""" Vincenzo Passariello - Es1 - Lab04 """

import string

def isPalindrome(s):
    s = s.translate(str.maketrans("", "", string.whitespace))
    s = s.translate(str.maketrans("", "", string.punctuation))
    r = s[::-1]
    l1 = []
    l2 = []
    for i in s:
        l1.append(i)
    for j in r:
        l2.append(j)
    if l1 == l2:
        return True
