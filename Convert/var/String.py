import Utilis

def stringToNum(String: str):
    try:
        return float(String)
    except ValueError:
        nums = [ord(letter) for letter in String]
  
        return Utilis.Convert.var.listToString(nums)  # Gibt die lange Zahlenkette als Text zurück

def stringToList(String:str):
    return list(String)
def stringToDic(String:str):
    String = list(String)
    output = {}
    for part in range(len(String)):
        output[part] = String[part]
    return output
def stringToTuple(String:str):
    return tuple(String
)
