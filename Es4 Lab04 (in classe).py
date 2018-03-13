def mediaVoti(t):
    lista_voti = []
    for i in t:
        lista_voti.append(i)
    media = sum(lista_voti)/len(t)
    return(media)

t = ()
try:
    t = eval(input("Questo programma calcola la media di una tupla di voti numerici. Inserisci una tupla di numeri: "))
    if((type(t) is int) or (type(t) is float)):
        print("La media è:", t)
    else:
        print("La media è:", mediaVoti(t))
except(SyntaxError, ValueError):
    print("Errore!")
