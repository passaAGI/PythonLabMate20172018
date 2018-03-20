""" Vincenzo Passariello - Es2 - Lab06 """

import sys

def isPrime(n):
    i = 2
    flag = True
    while flag:
        if(n%i == 0):
            return False
        else:
            i += 1
            if(n%i != 0):
                return True

print(isPrime(7))
