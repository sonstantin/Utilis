def fibonacci(start: float, times:int):
    first = start
    second = start
    list = []
    for i in range(times):
        number = first + second
        print(f"{i+1}) {first:.2f} + {second:.2f} = {number:.2f}")
        list.append(number)
        first = second
        second = number
    return list


if __name__ == "__main__":
    start = float(input("Gib eine Zahl ein: "))
    times = int(input("Gib die Zahl der Wiederholungen an: "))
    output = fibonacci(start, times)
    print(output)
    
