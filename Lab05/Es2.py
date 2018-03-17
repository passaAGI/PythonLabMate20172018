""" Vincenzo Passariello - Es2 - Lab05 """

def gcd(n, m):
    if(n != 0 and m != 0):
        n = abs(n)
        m = abs(m)
        d_n = []
        d_m = []
        d_nm = []
        for i in range(1, n+1):
            if n%i == 0:
                d_n.append(i)
        for j in range(1, m+1):
            if m%j == 0:
                d_m.append(j)
        for i in d_n:
            if i in d_m:
                d_nm.append(i)
        return(max(d_nm))
    elif(n == 0 or m == 0):
        return("Error!")
