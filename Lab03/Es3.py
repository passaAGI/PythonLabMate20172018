""" Vincenzo Passariello - Es3 - Lab03 """

def noleggioScooter(giorni):
    tariffa = 40
    if(giorni < 1):
        return(0.0)
    elif(giorni >= 1):
        if(giorni == 1):
            return(float(tariffa + 5))
        else:
            return(float(tariffa*giorni))

days = float(input("Per quanti giorni desideri noleggiare lo scooter? "))
print("Il costo è di", noleggioScooter(days), "euro")
