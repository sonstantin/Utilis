import io, PIL
from PIL import ImageTk, Image
import Utilis
def PNGToTK(png:str):
    image_stream = io.BytesIO(png)
    pil_img = Image.open(image_stream)

    
    tk_img = ImageTk.PhotoImage(pil_img)
    return tk_img
if __name__ == "__main__":
    PNGToTK(png=Utilis.Convert.image.SVGToPNG.svg_to_png(input="noodle-bowl.svg", var=True))
