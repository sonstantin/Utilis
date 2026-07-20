import Utilis

def NumToString(Num:float):
    return str(Num)
def NumToList(Num:float, mode:str="normal"):
        if mode == "normal":
            return [Num]
        else:
            List = (list(range(int(Num))))
            List.append(Num)
            return List
def NumToTuple(Num:float, mode:str="normal"):
        if mode == "normal":
            return (Num)
        else:
            Tuple = (list(range(Num)))
            Tuple.append(Num)
            return tuple(Tuple)
def NumToDic(Num:float):
    NumList = NumToList(Num, "")
    dic = {}
    for num in NumList:
        if not num == Num:
            dic[num] = False
        else:
            dic[num] = True
    return dic

    
