""" Vincenzo Passariello - Es1 - Lab06 """

import sys

print("***Gestione voti studente***")
print("- Inserimento voto (1)")
print("- Visualizzazione voti (2)")
print("- Stampa media voti (3)")
print("- Terminazione programma (0)")

def avg(marks):
    average = sum(marks)/len(marks)
    return(average)

marks = []
flag = True
while flag:
    ans = int(input("Scelta: "))
    if(ans == 1):
        mark = int(input("Inserisci un voto: "))
        marks.append(mark)
    elif(ans == 2):
        print(tuple(marks))
    elif(ans == 3):
        print(avg(marks))
    elif(ans == 0):
        flag = False
        sys.exit()
    else:
        print("Azione non consentita!")
