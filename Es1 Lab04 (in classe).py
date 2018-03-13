import string

def stringPolishing(s):
    str(s)
    for i in s:
        s = s.translate(str.maketrans("", "", string.whitespace))
        s = s.translate(str.maketrans("", "", string.punctuation))
    return(s)
