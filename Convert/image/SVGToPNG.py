import os
import re
import math
import io
import sys
import argparse
import xml.etree.ElementTree as ET
import png
from svgpathtools import parse_path

def svg_to_png(input:str, var:bool=False, output:str="output.png", width:int=400, height:int=400, supersample:int=2):
    """
    Rendert ein SVG (Dateipfad oder XML-String) in ein transparentes PNG.
    """
    def hex_to_rgba(color_str):
        if not color_str or color_str.lower() == 'none':
            return None
        color_str = color_str.lstrip('#')
        try:
            if len(color_str) == 3:
                color_str = ''.join([c*2 for c in color_str])
            return (
                int(color_str[0:2], 16),
                int(color_str[2:4], 16),
                int(color_str[4:6], 16),
                255
            )
        except ValueError:
            return None

    def get_style(elem, attr, css_dict, default=None):
        val = elem.attrib.get(attr)
        if val is not None:
            return val
        style = elem.attrib.get('style', '')
        match = re.search(fr'{attr}\s*:\s*([^;]+)', style)
        if match:
            return match.group(1).strip()
        elem_class = elem.attrib.get('class')
        if elem_class and elem_class in css_dict and attr in css_dict[elem_class]:
            return css_dict[elem_class][attr]
        return default

    # Input verarbeiten (Datei oder Inline-XML)
    if os.path.exists(input):
        tree = ET.parse(input)
        root = tree.getroot()
    else:
        root = ET.fromstring(input)

    css_classes = {}
    for elem in root.iter():
        if elem.tag.endswith('style') and elem.text:
            rules = re.findall(r'\.([\w-]+)\s*\{([^}]+)\}', elem.text)
            for class_name, css_content in rules:
                styles = {}
                for item in css_content.split(';'):
                    if ':' in item:
                        k, v = item.split(':', 1)
                        styles[k.strip()] = v.strip()
                css_classes[class_name] = styles

    viewbox = root.attrib.get('viewBox')
    if viewbox:
        vx, vy, vw, vh = map(float, viewbox.split())
    else:
        vx, vy = 0.0, 0.0
        vw = float(root.attrib.get('width', width))
        vh = float(root.attrib.get('height', height))

    sw, sh = width * supersample, height * supersample
    scale = min((sw - 40 * supersample) / vw, (sh - 40 * supersample) / vh)
    offset_x = (sw - (vw * scale)) / 2 - (vx * scale)
    offset_y = (sh - (vh * scale)) / 2 - (vy * scale)

    buffer = bytearray([0]) * (sw * sh * 4)

    for elem in root.iter():
        tag = elem.tag.split('}')[-1]
        lines = []

        if tag == 'path':
            d = elem.attrib.get('d')
            if d:
                path = parse_path(d)
                for segment in path:
                    steps = max(4, int(segment.length() * scale))
                    pts = [segment.point(i / steps) for i in range(steps + 1)]
                    for i in range(len(pts) - 1):
                        p1, p2 = pts[i], pts[i+1]
                        lines.append((
                            (p1.real * scale + offset_x, p1.imag * scale + offset_y),
                            (p2.real * scale + offset_x, p2.imag * scale + offset_y)
                        ))
        elif tag == 'rect':
            x = float(elem.attrib.get('x', 0)) * scale + offset_x
            y = float(elem.attrib.get('y', 0)) * scale + offset_y
            w_elem = float(elem.attrib.get('width', 0)) * scale
            h_elem = float(elem.attrib.get('height', 0)) * scale
            pts = [(x, y), (x + w_elem, y), (x + w_elem, y + h_elem), (x, y + h_elem), (x, y)]
            for i in range(4):
                lines.append((pts[i], pts[i+1]))
        elif tag == 'circle':
            cx = float(elem.attrib.get('cx', 0)) * scale + offset_x
            cy = float(elem.attrib.get('cy', 0)) * scale + offset_y
            r = float(elem.attrib.get('r', 0)) * scale
            steps = max(16, int(2 * math.pi * r))
            pts = [(cx + r * math.cos(2 * math.pi * i / steps), 
                    cy + r * math.sin(2 * math.pi * i / steps)) for i in range(steps + 1)]
            for i in range(steps):
                lines.append((pts[i], pts[i+1]))

        if not lines:
            continue

        fill_str = get_style(elem, 'fill', css_classes, default='#000000')
        stroke_str = get_style(elem, 'stroke', css_classes, default='none')
        stroke_w_str = get_style(elem, 'stroke-width', css_classes, default='1')

        fill_rgba = hex_to_rgba(fill_str)
        stroke_rgba = hex_to_rgba(stroke_str)
        stroke_width = max(1, int(float(stroke_w_str) * scale))

        if fill_rgba:
            min_y = max(0, int(min(min(y1, y2) for (_, y1), (_, y2) in lines)))
            max_y = min(sh, int(max(max(y1, y2) for (_, y1), (_, y2) in lines)) + 1)

            for y in range(min_y, max_y):
                scan_y = y + 0.5
                intersections = []
                for (x1, y1), (x2, y2) in lines:
                    if (y1 <= scan_y < y2) or (y2 <= scan_y < y1):
                        intersections.append(x1 + (scan_y - y1) * (x2 - x1) / (y2 - y1))

                intersections.sort()
                row_offset = y * sw * 4

                for i in range(0, len(intersections) - 1, 2):
                    x_start = max(0, min(sw, int(intersections[i])))
                    x_end = max(0, min(sw, int(intersections[i+1])))
                    for x in range(x_start, x_end):
                        idx = row_offset + (x * 4)
                        buffer[idx:idx+4] = fill_rgba

        if stroke_rgba:
            half_w = stroke_width // 2
            for (x1, y1), (x2, y2) in lines:
                steps = max(abs(x2 - x1), abs(y2 - y1))
                if steps == 0:
                    continue
                dx, dy = (x2 - x1) / steps, (y2 - y1) / steps
                cx, cy = x1, y1
                for _ in range(int(steps)):
                    px, py = int(cx), int(cy)
                    for wx in range(-half_w, half_w + 1):
                        for wy in range(-half_w, half_w + 1):
                            nx, ny = px + wx, py + wy
                            if 0 <= nx < sw and 0 <= ny < sh:
                                idx = (ny * sw + nx) * 4
                                buffer[idx:idx+4] = stroke_rgba
                    cx += dx
                    cy += dy

    final_pixels = []
    factor = supersample * supersample
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = 0, 0, 0, 0
            for sy in range(supersample):
                for sx in range(supersample):
                    idx = ((y * supersample + sy) * sw + (x * supersample + sx)) * 4
                    r += buffer[idx]
                    g += buffer[idx+1]
                    b += buffer[idx+2]
                    a += buffer[idx+3]
            row.extend([r // factor, g // factor, b // factor, a // factor])
        final_pixels.append(row)

    w = png.Writer(width, height, greyscale=False, alpha=True, bitdepth=8)

    if var == False:
        with open(output, 'wb') as f:
            w.write(f, final_pixels)
        return True
    else:
        output_stream = io.BytesIO()
        w.write(output_stream, final_pixels)
        return output_stream.getvalue()

if __name__ == "__main__":
    # Standard-Eingabe ohne Terminal-Argumente
    input_file = input()   # Hier deine SVG-Datei eintragen
    output_file = input()  # Hier den Wunsch-Namen eintragen
    
    svg_to_png(input_file, output=output_file)
    print("Fertig!")
