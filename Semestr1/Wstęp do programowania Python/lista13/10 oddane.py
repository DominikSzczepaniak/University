wejscie = input()
wejscie = list(wejscie)
caly_wynik = []
wynik = []
do_tablicy = False
for i in range(1, len(wejscie)-1):
    if(wejscie[i] == " "):
        continue 
    elif(wejscie[i] == "("):
        do_tablicy = True 
        wynik = []
    elif(wejscie[i] == ")"):
        do_tablicy = False 
        caly_wynik.append(wynik)
        wynik = []
    else:
        if(do_tablicy == False):
            caly_wynik.append(wejscie[i])
        else:
            wynik.append(wejscie[i])
print(caly_wynik)

def dodaj(lista):
    wynik = 0
    for i in lista:
        if(type(i) == list):
            wynik += int(oblicz_wartosc(i))
            print(oblicz_wartosc(i))
        else:
            wynik += int(i)
    return wynik
def odejmij(lista):
    wynik = 0
    if(type(lista[0]) == list):
        wynik = int(oblicz_wartosc(lista[0]))
    else:
        wynik = int(lista[0])
    for i in lista[1:]:
        if(type(i) == list):
            wartosc = oblicz_wartosc(i)
            wynik -= int(wartosc)
        else:
            wynik -= int(i)
    return wynik 
def pomnoz(lista):
    wynik = 1
    for i in lista:
        if(type(i) == list):
            wynik *= int(oblicz_wartosc(i))
        else:
            wynik *= int(i)
    return wynik
def podziel(lista):
    wynik = 0
    if(type(lista[0]) == list):
        wynik = int(oblicz_wartosc(lista[0]))
    else:
        wynik = int(lista[0])
    for i in lista[1:]:
        if(type(i) == list):
            wartosc = oblicz_wartosc(i)
            wynik /= int(wartosc)
        else:
            wynik /= int(i)
    return wynik 

def oblicz_wartosc(tablica):
    operacja = tablica[0]
    if(operacja == "+"):
        return dodaj(tablica[1:])
    elif(operacja == "-"):
        return odejmij(tablica[1:])
    elif(operacja == "*"):
        return pomnoz(tablica[1:])
    elif(operacja == "/"):
        return podziel(tablica[1:])
    

typ = caly_wynik[0]
wynik = 0
if(typ == "+"):
    wynik = dodaj(caly_wynik[1:])
elif(typ == "-"):
    wynik = odejmij(caly_wynik[1:])
elif(typ == "*"):
    wynik = pomnoz(caly_wynik[1:])
elif(typ == "/"):
    wynik = podziel(caly_wynik[1:])
print(wynik)