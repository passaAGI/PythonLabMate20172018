""" Vincenzo Passariello - Es1 - Lab03 """

def rootFinder(a, b, c):
    delta = ((b*b)-4*a*c)
    if(a == 0): #non è di secondo grado
        if((b == 0) and (c == 0)):
            print("L'equazione è indeterminata!")
            return None
        elif(b == 0):
            print("L'equazione non ammette soluzioni reali!")
            return None
        else:
            return float(-c/b)
    if(a != 0):
        if(delta) < 0:
            print("L'equazione non ammette soluzioni reali!")
            return None
        elif(delta) >= 0:
            x1 = float((-b-(math.sqrt(delta)))/2*a)
            return(x1)
            x2 = float((-b+(math.sqrt(delta)))/2*a)
            return(x2)
