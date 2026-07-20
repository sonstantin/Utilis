def ggt(first: float, second: float):
    # Wir stellen sicher, dass 'a' die größere Zahl ist
    a, b = sorted([first, second], reverse=True)
    
    while b != 0:
        # a wird zu b, und b wird zum Rest aus a % b
        a, b = b, a % b
        
    return a
def kgv(first:float, second:float):
    multiplied = first * second
    divide = ggt(first,second)
    return multiplied / divide
    
if __name__ == "__main__":
    first = int(input("Zahl 1: "))
    second = int(input("Zahl 2: "))
    print(f"ggT: {ggt(first, second)}")
    print(f"kgV: {kgv(first, second)}")
    
