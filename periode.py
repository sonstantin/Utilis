def seeperiod(first: int, second: int):
    # Vor dem Komma berechnen
    vorkomma = first // second
    rest = first % second
    
    # Wenn die Division sofort aufgeht (z.B. 4 / 2)
    if rest == 0:
        return None

    nachkommastellen = []
    gesehene_reste = {}  # Hier merken wir uns: {Rest: Position_im_Ergebnis}

    while rest != 0:
        # MATHEMATISCHER TRICK: Haben wir exakt diesen Rest schon einmal gesehen?
        if rest in gesehene_reste:
            start_periode = gesehene_reste[rest]
            
            vor_periode = nachkommastellen[:start_periode]
            periodischer_teil = nachkommastellen[start_periode:]
            string = ""
            for num in periodischer_teil:
                string += num
            # Wir geben zurück: (Index des Starts, Stellen davor, periodische Stellen)
            return (start_periode, int(string))

        # Rest merken und seine aktuelle Position abspeichern
        gesehene_reste[rest] = len(nachkommastellen)

        # Schriftliche Division: Rest mal 10 nehmen
        rest *= 10
        nächste_ziffer = rest // second
        nachkommastellen.append(str(nächste_ziffer))

        # Neuen Rest für die nächste Runde berechnen
        rest = rest % second

    # Wenn die Schleife beendet wird, weil der Rest 0 wurde (z.B. 1/4 = 0.25)
    return False


if __name__ == "__main__":
    try:
        zahl1 = int(input("Zahl 1 (Zähler): "))
        zahl2 = int(input("Zahl 2 (Nenner): "))
        
        ergebnis = seeperiod(zahl1, zahl2)
        print(f"Rückgabewert der Funktion: {ergebnis}")
        
    except EOFError:
        print("Interaktive Eingabe im Editor blockiert. Starte automatischen Test mit 1 und 6:")
        print(seeperiod
(1, 6))
