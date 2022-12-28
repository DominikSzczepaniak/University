#Advent of code 2022 day 5
wejscie = []
for line in open("input.txt"):
    tablica = []
    for s in line:
        tablica.append(s)
    wejscie.append(tablica)
ilosc_stakow = 0
wysokosc = 0
for i in range(len(wejscie)):
    try:
        if(wejscie[i][1] == '1'):
            wysokosc = i
            ilosc_stakow = max(wejscie[i])
    except IndexError:
        continue 



tablica = []
for i in range(wysokosc-1, -1, -1):
    for j in range(int(ilosc_stakow)):
        litera = wejscie[i][1+j*4]
        if(litera == ' '):
            continue
        if(i==wysokosc-1):
            tablica.append([litera])
        else:
            tablica[j].append(litera)
wejscie2 = []
linia = -1
for line in open("input.txt"):
    linia += 1
    slowa_tablica = []
    for slowa in line.rsplit():
        slowa_tablica.append(slowa)
    wejscie2.append(slowa_tablica)
ile_done = 0
print(wejscie2)
for i in wejscie2:
    try:
        if(i[0] == "move"):
            ile_done += 1
            ile = int(i[1])
            skad = int(i[3])-1
            dokad = int(i[5])-1
            lista = []
            ilosc_przeniesiona = 0
            for i in range( int(len(tablica[skad]) - 1), -1, -1):
                lista.append(tablica[skad][i])
                tablica[skad].pop()
                ilosc_przeniesiona+=1
                if(ilosc_przeniesiona == ile):
                    break 
            for i in lista:
                tablica[dokad].append(i)
    except IndexError:
        continue
for i in range(len(tablica)):
    print(tablica[i][-1])