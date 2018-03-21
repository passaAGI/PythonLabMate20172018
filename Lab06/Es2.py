""" Vincenzo Passariello - Es2 - Lab06 """

import sys

def isPrime(n):
    i = 2
    if(n == 1):
        return False
    while n > i:
        if(n%i == 0 & i != n):
            return False
            break
        i += 1
    else:
        return True
