""" Vincenzo Passariello - Es1 - Lab04 """

def tupleMod(t1, t2, n):
    lst = list(t1)
    lst2 = list(t2)
    lst2.reverse()
    for i in range(0, len(lst2)):
        lst.insert(n, lst2[i])
    return(tuple(lst))

