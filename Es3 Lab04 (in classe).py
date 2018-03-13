stringa = str(input("Stringa: "))
carattere = str(input("Carattere: "))
if carattere not in stringa:
    print("Il carattere", carattere, "compare 0 volte nella stringa", stringa)
elif carattere in stringa:
    print("Il carattere", carattere, "compare", stringa.count(carattere), "volte nella stringa", stringa)
    
    
        
        
    
