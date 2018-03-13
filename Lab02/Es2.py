""" Vincenzo Passariello - Es2 - Lab02 """

import math

def capitaleFinale(C, r, n, t):
    M = C*pow(1+(r/n), n*t)
    return M

C = 10000
r = 0.08
n = 12
t = 2
print("Capitale finale per investimento di", C, ", calcolo mensile, tasso di", int(r*100), "%, per", t, "anni:", capitaleFinale(C, r, n, t))
