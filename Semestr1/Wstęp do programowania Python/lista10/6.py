from collections import defaultdict as dd
from random import choice, randint
imiona = []
for linia in open("imiona.txt"):
    imiona.append(linia.split("-")[0])
po = dd(lambda: [])
po2 = dd(lambda: [])
pierwsze_litery = []
for imie in imiona:
    pierwsze_litery.append(imie[0])
    for j in range(len(imie)-1):
        po[imie[j]].append(imie[j+1])
        if(j!= len(imie)-2):
            po2[imie[j]].append(imie[j+2])
dlugosc_minimalna = 4
dlugosc_maksymalna = 8
pierwsza_litera = choice(pierwsze_litery)
druga_litera = choice(po[pierwsza_litera])
imie = [pierwsza_litera, druga_litera]
dlugosc = randint(dlugosc_minimalna, dlugosc_maksymalna)
for i in range(2, dlugosc):
    imie.append(choice(po[imie[i-1]] + po2[imie[i-2]]))
imie = [i.lower() for i in imie]
imie[0] = imie[0].upper()
print("".join(imie))#.split("[")[0])