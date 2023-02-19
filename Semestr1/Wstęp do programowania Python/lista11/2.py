from collections import defaultdict as dd
def slowo_na_cyfre(slowo):
    slownik = dd(lambda: 0)
    wartosc = 1
    for litera in slowo:
        if(slownik[litera] == 0):
            slownik[litera] = wartosc 
            wartosc += 1
    wynik = ""
    for id, litera in enumerate(slowo):
        wynik += str(slownik[litera])
        if(id != len(slowo)-1):
            wynik += str("-")
    return wynik
print(slowo_na_cyfre("tak"))
print(slowo_na_cyfre("nie"))
print(slowo_na_cyfre("tata"))
print(slowo_na_cyfre("indianin"))
        