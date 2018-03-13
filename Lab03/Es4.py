""" Vincenzo Passariello - Es4 - Lab03 """

def pasquaCalc(anno):
    a = divmod(anno, 100)
    b = divmod(5*a[0]+a[1], 19)
    c = divmod(3*(a[0]+25), 4)
    d = divmod(8*(a[0]+11), 25)
    e = divmod(19*b[1]+c[0]-d[0], 30)
    f = divmod(b[1]+11*e[1], 319)
    g = divmod(60*(5-c[1])+a[1], 4) 
    h = divmod(2*g[0]-g[1]-e[1]+f[0], 7)
    i = divmod(e[1]-f[0]+h[1]+110, 30)
    j = divmod(i[1]+5-i[0], 32)
    n = j[1]
    p = i[0]
    return(n, p)
