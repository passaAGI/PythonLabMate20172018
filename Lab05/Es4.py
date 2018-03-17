""" Vincenzo Passariello - Es4 - Lab05 """

import turtle
import random

def starDrawer(n):
    if(n >= 7):
        q = leastCoprime(n)
        for i in range(n):
            turtle.forward(100)
            turtle.right((360/n)*q)

def leastCoprime(n):
    c = []
    if n > 2:
        for i in range(2, n):
           if(gcd(n,i)==1):
               c.append(i)
               break
        return(min(c))

def gcd(n, m):
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
