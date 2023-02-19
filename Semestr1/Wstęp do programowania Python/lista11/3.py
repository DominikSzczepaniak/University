import matplotlib
import numpy
import pandas as pd 

data = pd.read_csv("wyniki.txt", sep = "\t")
wszystkie_komitety = []
nazwy_komitetow = []
laczna_ilosc_mandatow = dict()
for nazwa in data:
    if(nazwa in {"Nazwa", "NR", "Inni", "Wlk"}):
        continue
    nazwy_komitetow.append(nazwa)
    laczna_ilosc_mandatow[nazwa] = 0

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
        laczna_ilosc_mandatow[wyniki[len(wyniki)-1-i][1]] += 1
        suma += 1
print(suma)
for komitet in laczna_ilosc_mandatow:
    print(f"Komitet {komitet} otrzymał {laczna_ilosc_mandatow[komitet]} mandatów")
