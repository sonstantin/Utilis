def listToString(List:list):
    string = ""
    for part in List:
        string += str(part)
    return string

def listToNum(List:list):
    string = listToString(List)
    return float(string)
def listToDic(List:list):
    dic = {}
    for i in range(len(List)):
        dic[i] = List[i]
    return dic
def listToTuple(List:list):
    return tuple(List)
def listToBool(List:list=None):
    if List == None:
        return None
    try:
        if len(List) == 0:
            return False
        else:
            return True
    except NameError:
        return None
    

