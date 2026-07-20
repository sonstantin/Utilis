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
def root(num:float, schritte:int=100):
    estimated = num / 2.0
    for i in range(schritte):
        estimated = 0.5 * (estimated+ num / estimated)
        if __name__ == "__main__":
            print(f"{i+1}) {estimated}")
    return estimated
def round(num:float, how:str="normal"):
    lower_num = num // 1
    if __name__ == "__main__":
        print(lower_num)
    if how == "down":
        return lower_num
    elif how == "up":
        return lower_num + 1
    else:
        decimal =  num - lower_num
        if decimal < 0.5:
            return lower_num
        else:
            return lower_num + 1
    
if __name__ == "__main__":
    liste = [1,2,3]
    value = add(liste)
    print(value)
    
    integer = 12
    value = substract(integer, liste)
    print(value)
    
    liste = [1,2,3]
    value = multiply(liste)
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
    
    num = float(input("Um welche Wurzel geht es? "))
    print(root(num))
    
   
