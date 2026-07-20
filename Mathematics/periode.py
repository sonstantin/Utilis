from fractions import Fraction

def seeperiod(first: int, second: int):
    rest = first % second
    
    if rest == 0:
        return None

    nachkommastellen = []
    gesehene_reste = {}

    while rest != 0:
        if rest in gesehene_reste:
            start_periode = gesehene_reste[rest]
            
            periodischer_teil = nachkommastellen[start_periode:]
            string = "".join(periodischer_teil)
            
            # REPARATUR 1: Wir geben die Periode als STRING zurück,
            # damit führende Nullen (wie bei 1/97) nicht gelöscht werden!
            return (start_periode, string)

        gesehene_reste[rest] = len(nachkommastellen)

        rest *= 10
        nächste_ziffer = rest // second
        nachkommastellen.append(str(nächste_ziffer))
        rest = rest % second

    return False

def resolve_periode(periode: tuple):
    # REPARATUR 2: periode[1] ist jetzt bereits ein String.
    try:
        stringperiode = periode[1]
    except TypeError:
        return None
    PeriodeLen = len(stringperiode)
    
    # REPARATUR 3: Erstelle einen String aus genau so vielen Neunen,
    # wie die Periode lang ist (z.B. "9" * 96)
    neunen_string = "9" * PeriodeLen
    
    # Wir wandeln erst hier für die Fraction in Ganzzahlen um
    return Fraction(int(stringperiode), int(neunen_string))

if __name__ == "__main__":
    try:
        zahl1 = int(input("Zahl 1 (Zähler): "))
        zahl2 = int(input("Zahl 2 (Nenner): "))
        
        ergebnis = seeperiod(zahl1, zahl2)
        print(f"Rückgabewert der Funktion seeperiod: {ergebnis}")
        
        if ergebnis and ergebnis != True:
            bruch = resolve_periode(ergebnis)
            print(f"{ergebnis}")
            print(f"Rückgabewert der Funktion resolve_periode: {bruch}")
        else:
            print("Keine Periode vorhanden oder Division geht auf.")
        
    except EOFError:
        print("Interaktive Eingabe im Editor blockiert. Starte automatischen Test mit 1 und 6:")
        per = seeperiod(1, 6)
        print(per)
        print(resolve_perio
              de(per))
