def fibonacci(start: float, times:int, round:int=2, show:bool=False):
    first = start
    second = start
    list = []
    try:
        for i in range(times):
            number = first + second
            if __name__ == "__main__" or show == True:
                print(f"{i+1}) {first:.{round}f} + {second:.{round}f} = {number:.{round}f}")
            list.append(number)
            first = second
            second = number
        return list
    except ValueError:
        raise ValueError("Input Integers for times and round!")


if __name__ == "__main__":
    start = float(input("Gib eine Zahl ein: "))
    times = int(input("Gib die Zahl der Wiederholungen an: "))
    Toround = int(input("Gib die Anzahl der Nachkommastellen an: "))
    output = fibonacci(start, times, Toround)
    print(output)
    
