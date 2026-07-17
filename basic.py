def add(toadd:list):
    output = 0
    for num in toadd:
        try:
            output += num
        except TypeError:
            raise TypeError("Input has to be an Integer or a float")
    return output
def substract(first:float,tominus:list):
    output = first
    for num in tominus:
        output -= num
    return output
def multiply(tomulti:list):
    output = 1
    for num in tomulti:
        output = output * num
    return output
def devide(first:float, second:float):
    return first / second
def floor(first:float, second:float):
    return first // second
def modulo(first:float, second:float):
    return first % second
def devideFull(first:float, second:float):
    return {"Devide": first / second,
    "Floor": first // second,
    "Modulo": first % second}
def extrapolation(first: float, second:int, show: bool = False):
    num = 1
    for i in range(second):
        num *= first
        if __name__ == "__main__" or show == True:
            print(num)
    return num
    
if __name__ == "__main__":
    list = [1,2,3]
    value = add(list)
    print(value)
    
    integer = 12
    value = substract(integer, list)
    print(value)
    
    list = [1,2,3]
    value = multiply(list)
    print(value)
    
    first = 1
    second = 97
    
    value = devide(first, second)
    print(value)
    
    value = floor(first, second)
    print(value)
    
    value = modulo(16, 10)
    print(value)
    
    value = devideFull(first, second)
    print(value)
    
    value = extrapolation(2.5,8)
    print(value)
