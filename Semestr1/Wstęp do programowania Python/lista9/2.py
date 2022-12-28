from collections import defaultdict as dd
#pomysly:
#wszystkie wyrazy zamienic na slowniki, te slowniki pozniej na hashe i wrzucic to do slownika, gdzie kluczem jest hash, a wynikiem jest tablica slow (czyli dla kazdego hasha jest okreslona jakas kombinacja liter i wszystkie slowa ktore maja taka kombinacje liter maja ten sam hash i mozemy je bardzo szybko odszukac)

#1. wszystkie pary slow w O(n^2), zlaczyc te pary w jeden slownik, od ilosci liter z wejscia odjac ilosc liter w parze tych slow - mamy slownik z pozostalymi literami ktore chcemy miec w slowie. zmieniamy ten slownik w hash i odwolujemy sie do slownika z tablicami slow dla odpowiedniego hasha

#2. sprawdzic wszystkie mozliwosci podzialu wejsciowego slowa. czyli np. bas - pierwszy wyraz moze miec b/a/s drugi a/b/s, trzeci s/a/b
# tzn. kazdy wyraz dzielimy na odpowiednia ilosc wystapien kazdej litery. czyli jak mamy bbb to mozemy miec:
#003
#030
#300
#012
#102
#
#111   
# gdzie miejsce oznacza ktore slowo. Gdy zrobimy tak z kazda litera to otrzymamy liste liter ktore ma dane slowo, wrzucamy to do slownika, hashujemy i czytamy z tablicy cyz istnieja takie trzy slowa ktore maja odpowiednie ilosci liter, jesli tak to mamy nasze trzy slowa
# jaka tu bedzie zlozonosc? zalezy od wystapien odpowiednich liter, ale mysle ze przy slowie o dlugosci 20 bedzie to <=10^7 na wszystkie opcje, wiec jest szansa ze sie zmiesci w przedziale czasowym. 
# + tego rozwiazania jest taki ze bazuje na dlugosci wejscia, a nie na wielkosci listy slow




p = 31
mod = int(1e9+7)
potegi = [1]
for i in range(300):
    potegi.append((potegi[-1]*p)%mod)
def dictHashing(slownik):
    wynik = 1
    for keys, value in slownik.items():
        try:
            wynik = ((wynik*potegi[ord(keys.lower())-97]%mod)*value%mod)
        except:
            return -1
    return wynik 

#rozklad imienia i nazwiska na slownik + hashowanie
imie_nazwisko = input("Podaj imie nazwisko:")
rozklad_wejscia = dd(lambda: 0)
for wyrazy in imie_nazwisko.rsplit():
    for litera in wyrazy:
        rozklad_wejscia[litera]+=1 
hash_wejscia = dictHashing(rozklad_wejscia)

#rozklad slow na slowniki i pozniej hashowanie tych slownikow 
#z tych hashy robimy liste slow ktore maja takie same litery (slownik ktory w kluczu przyjmuje wartosc hasha, a w wyjsciu podaje liste slow)
litery_slowa = dd(lambda:[])
rozlozenie_slow_na_litery = dd(lambda:dd(0))
id = []

licznik = 0
for line in open("popularne_slowa.txt"):
    for slowo in line.rsplit():
        id.append(slowo)
        wyraz = dd(lambda: 0)
        for litera in slowo:
            wyraz[litera] += 1
        rozlozenie_slow_na_litery[slowo] = wyraz 
        wartosc_hash = dictHashing(wyraz)
        if(wartosc_hash == -1):
            continue 
        litery_slowa[dictHashing(wyraz)] += slowo

#przejdzmy po mozliwych ilosciach wystapien kazdej z liter
def mozliwosci_laczen(n): 
    mozliwosci = []
    for i in range(0, n+1):
        for j in range(0, n+1):
            for k in range(0, n+1):
                if(i + j + k == n):
                    mozliwosci.append([i, j, k]) 
    return mozliwosci

opcje = dd(lambda: [])
licznik = 0
for litera, ilosc in rozklad_wejscia.items():
    opcje[litera] = mozliwosci_laczen(ilosc)
#dla kazdej litery chcemy wziac wszystkie mozliwosci i polaczyc to w jedna mozliwosc do kolejnej opcji?
#czyli jak mamy 'b': [[0, 0, 1], [0, 1, 0], [1, 0, 0]] i  'o': [[0, 0, 1], [0, 1, 0], [1, 0, 0]] to chcemy wynik: [[[0, 0, 1],[0, 0, 1]], [[0, 0, 1], [0, 1, 0]], [[0, 0, 1] ],
ostatnia_litera = 0  
jaka_litera = []
wynik = []
for litera, tablice in opcje.items():
    if(licznik == 0):
        ostatnia_litera = litera 
        continue 
    for tablice in opcje[ostatnia_litera]:
        pass



