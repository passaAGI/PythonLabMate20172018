import time
import random

n = 1
m = 100
r = random.randint(n, m)
flag = True
trials = 0

print("Pensa ad un numero compreso tra 1 e 100")
time.sleep(2)
while flag:
    r = random.randint(n,m)
    print("Il numero da te pensato è", r, "?: ")
    ans = input()
    if(("grande" in ans) or ("Grande" in ans)):
        trials += 1
        m = r-1
    elif(("piccolo" in ans) or ("Piccolo" in ans)):
        trials += 1
        n = r+1
    elif(("indovinato" in ans) or ("Indovinato" in ans)):
        trials += 1
        flag = False
        print(trials)
