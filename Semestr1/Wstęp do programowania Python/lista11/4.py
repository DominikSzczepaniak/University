import matplotlib
import numpy
import pandas as pd 
import more_itertools
from collections import defaultdict as dd
from copy import deepcopy
def partition2(n):
    lst = [i for i in range(1, n+1)]
    for i in [podzial for ilosc in range(1, len(lst) + 1) for podzial in more_itertools.set_partitions(lst, ilosc)]:
        yield sorted(i)
mozliwe_sojusze = []
for i in partition2(6):
    mozliwe_sojusze.append(i)


data = pd.read_csv("wyniki.txt", sep = "\t")
wszystkie_komitety = []
nazwy_komitetow = []
komitet_na_numer = dict()
numer_na_komitet = dict()
numer = 1
for nazwa in data:
    if(nazwa in {"Nazwa", "NR", "Inni", "Wlk"}):
        continue
    nazwy_komitetow.append(nazwa)
    komitet_na_numer[nazwa] = numer 
    numer_na_komitet[numer] = nazwa 
    numer+=1
a = []
b = [] #generalnie to bedzie pusty, bo pis ma 51% mandatow, wiec wszyscy pozostali razem nie dadza rady wygrac i tak

for mozliwosc in mozliwe_sojusze:
    ilosc_sojuszy = len(mozliwosc)
    sojusze = [[] for i in range(ilosc_sojuszy)] #jakie mamy sojusze (koalicje) i z jakich numerow sie skladaja
    for i in range(ilosc_sojuszy):
        sojusze[i] = mozliwosc[i]
    w_ktorym_sojuszu = dict()

    for i in range(ilosc_sojuszy):
        for k in range(1, 7):
            if(k in sojusze[i]):
                w_ktorym_sojuszu[k] = i
    laczna_ilosc_mandatow = dd(lambda: 0)
    suma = 0
    for index, row in data.iterrows():
        mandaty = row[2] 
        wyniki = []
        for komitet in nazwy_komitetow:
            for i in range(1, mandaty+1):
                try:
                    iloraz = float(row[komitet])/i
                    wyniki.append((iloraz, komitet))
                except:
                    break
        wyniki.sort()
        for i in range(mandaty):
            komitet = wyniki[len(wyniki)-1-i][1]
            komitet_numer = komitet_na_numer[komitet]
            numer_sojusz = w_ktorym_sojuszu[komitet_numer]
            laczna_ilosc_mandatow[numer_sojusz] += 1
            suma += 1
    for i in range(ilosc_sojuszy):
        if(laczna_ilosc_mandatow[i]/suma > 0.5): #wygrali
            wariant = mozliwosc
            zwyciezcy = sojusze[i]
            liczba_mandatow = laczna_ilosc_mandatow[i]
            if(1 in sojusze[i]): #pis byl w tym sojuszu, wiec nie wyswietlamy do a
                b.append((wariant, zwyciezcy, liczba_mandatow))
            if(1 not in sojusze[i]):
                a.append((wariant, zwyciezcy, liczba_mandatow))
for i in b:
    wariant = i[0]
    zwyciezcy = i[1]
    liczba_mandatow = i[2]
    for i in range(len(wariant)):
        if(len(wariant[i]) > 1):
            for j in range(len(wariant[i])):
                try:
                    wariant[i][j] = numer_na_komitet[wariant[i][j]]
                except:
                    pass
        else:
            try:
                wariant[i][0] = numer_na_komitet[wariant[i][0]]
            except:
                pass
    print(f"Wariant: {wariant} \n Zwyciezcy: {zwyciezcy}\n Ilość mandatów: {liczba_mandatow}")

