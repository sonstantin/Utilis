start = float(input("Gib eine Zahl ein: "))
times = int(input("Gib die Zahl der Wiederholungen an: "))
def fibonacci(start, times):
    first = start
    second = start
    for i in range(times):
        number = first + second
        print(f"{i+1}) {first:.2f} + {second:.2f} = {number:.2f}")
        first = second
        second = number
fibonacci(start, times)
