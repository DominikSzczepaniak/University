def nsp(lista_slow):
    lista_slow = [i.lower() for i in lista_slow]
    najdluzsza = 0
    slowo = ""
    for i in range(len(lista_slow)):
        start = 0
        end = len(lista_slow[i]) - 1 
        while(start < end):
            mid = (start+end)//2
            ilosc = 1
            for j in range(len(lista_slow)):
                if(i == j):
                    continue 
                if(lista_slow[j][0:mid] == lista_slow[i][0:mid]):
                    ilosc += 1
            if(ilosc >= 3):
                if(najdluzsza < mid):
                    najdluzsza = mid
                    slowo = lista_slow[i][0:mid]
                start = mid + 1
            else:
                end = mid - 1
    return slowo 

lista_slow = ["Cyprian", "cyberotoman", "cynik", "ceniąc",  "czule"]
print(nsp(lista_slow))