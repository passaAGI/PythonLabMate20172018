""" Vincenzo Passariello - Es4 - Lab06 """

import sys

def ciclo(A, k):
    if(type(A) == int):
        if(A == 0):
            print("Ciclica modulo", k)
            sys.exit()
        else:
            print("Non ciclica modulo", k)
            sys.exit()
    if(len(A) == 0):
        print("Ciclica modulo", k)
        sys.exit()
    i = 0
    n = 0
    while i != len(A)-1:
        if(A[0]) == (A[i+1]%k):
            n += 1
        else:
            print("Non ciclica modulo", k)
            break
        if(A[i+1] == (A[i]+1)%k):
            n += 1
        else:
            print("Non ciclica modulo", k)
            break
        i += 1
        if(n == len(A)):
            print("Ciclica modulo", k)
