start = int(input("Gib eine Zahl ein: "))
times = int(input("Gib die Zahl der Wiederholungen an: "))
first = start
second = start
for i in range(times):
    number = first + second
    print(f"{i+1}) {first} + {second} = {number}")
    first = second
    second = number
