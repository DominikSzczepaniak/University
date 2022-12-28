from itertools import product #https://stackoverflow.com/questions/14006867/python-itertools-permutations-how-to-include-repeating-characters

def is_prime(n):
    if(n==1):
        return True
    i = 2
    while(i*i <= n):
        if(n%i==0):
            return False
        i= i+1
    return True

def generuj_liczby(dlugosc_liczby, ilosc_siodemek):
    wzor = "7"*ilosc_siodemek
    granica = dlugosc_liczby - ilosc_siodemek
    liczby = set()
    do_dodania = [0,1,2,3,4,5,6,7,8,9]
    for i in range(granica+1):
        if(i == 0):
            for j in product(do_dodania, repeat=granica):
                liczba = wzor + "".join([str(z) for z in j])
                if(is_prime(int(liczba))):
                    liczby.add(int(liczba))
        else:
            for j in product(do_dodania, repeat=granica):
                if(j[0] == 0):
                    continue
                liczba = "".join([str(z) for z in j[0:i]]) + wzor + "".join([str(z) for z in j[i:]]) 
                if(is_prime(int(liczba))):
                    liczby.add(int(liczba))
    liczby = sorted(liczby)
    for i in liczby:
        print(i)
    print(len(liczby))

ilosc_siodemek = int(input("Wpisz ilość siódemek pod rząd:"))
dlugosc_liczby = int(input("Wpisz długość liczby:"))

generuj_liczby(dlugosc_liczby, ilosc_siodemek)

