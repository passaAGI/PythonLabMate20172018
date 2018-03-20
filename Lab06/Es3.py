""" Vincenzo Passariello - Es3 - Lab06 """

import string

def isPunct():
    i = 0
    n = 0
    ans = input("Stringa: ")
    ans = list(ans)
    while i != len(ans):
        if ans[i] in string.punctuation:
            n += 1
        i += 1
    print("Il numero di segni di punteggiatura è...")
    return(n)
