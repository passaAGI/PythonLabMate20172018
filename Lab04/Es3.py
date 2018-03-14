""" Vincenzo Passariello - Es3 - Lab04 """

import string

def f(s):
    vowels = "aeiouAEIOU"
    tot = 0
    for i in vowels:
        if i in s:
            tot += s.count(i)
    for i in s:
        s = s.translate(str.maketrans("", "", string.whitespace))
        s = s.translate(str.maketrans("", "", string.punctuation))
        if i in vowels:
            s = s.translate(str.maketrans("", "", vowels))
    print(s)
    print(tot)
