#https://skos.ii.uni.wroc.pl/pluginfile.php/54369/mod_resource/content/1/c8.pdf zad 4
from random import randint
import turtle 
from collections import deque
def kwadrat(bok, kolor):
    turtle.fillcolor(kolor)
    turtle.pencolor(kolor)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(bok)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(bok)


def koniec(mapa_hipsometryczna):
    for i in mapa_hipsometryczna:
        for j in i:
            if(j == 0):
                return False 
    return True


turtle.tracer(0,1)
minimalna_liczba_wzgorz = 50
maksymalna_liczba_wzgorz = 100

minimalna_wysokosc_wzgorza = 50
maksymalna_wysokosc_wzgorza = 120

minimalna_ilosc_pixeli_na_wzgorze = 50
maksymalna_ilosc_pixeli_na_wzgorze = 200


ile_wzgorz = randint(minimalna_liczba_wzgorz, maksymalna_liczba_wzgorz)
mapa = [[0 for i in range(100)] for j in range(100)]
kierunki4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]
kierunki8 = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, 1), (0,0)]
wielkosci = []
wysokosci = []
pixele_wzgorz = [[0] for i in range(ile_wzgorz)]

for i in range(ile_wzgorz):
    wielkosci.append(randint(minimalna_ilosc_pixeli_na_wzgorze, maksymalna_ilosc_pixeli_na_wzgorze))
    wysokosci.append(randint(minimalna_wysokosc_wzgorza, maksymalna_wysokosc_wzgorza))
for i in range(ile_wzgorz):
    pixele_wzgorz[i] = (randint(0, 99), randint(0,99))
for wzgorza in range(ile_wzgorz):
    #bfs dodajacy wokol miejsca startowego wzgorza odpowiednia ilosc punktow
    q = deque()
    odwiedzone = [[False for i in range(100)] for j in range(100)]
    q.append(pixele_wzgorz[wzgorza])
    ile = 1
    while(ile != wielkosci[i] and len(q) > 0):
        krotka = q.popleft()
        y = krotka[0]
        x = krotka[1]
        if(odwiedzone[y][x]):
            continue 
        odwiedzone[y][x] = True 
        ile += 1
        mapa[y][x] = wysokosci[wzgorza]
        pominac = randint(0, 3)
        ktore = -1
        for pion, poziom in kierunki4:
            ktore += 1
            if(ktore == pominac):
                continue
            try:
                if(odwiedzone[y+pion][x+poziom] == True):
                    continue 
                q.append((y+pion, x+poziom))
            except:
                pass
                


kolejka = deque()
odwiedzone = [[False for i in range(100)] for j in range(100)]
for j in range(ile_wzgorz):
    i = pixele_wzgorz[j]
    kolejka.append((i[0], i[1]))
while(len(kolejka) != 0):   
    krotka = kolejka.popleft()
    y = krotka[0]
    x = krotka[1]
    if(odwiedzone[y][x]):
        continue
    odwiedzone[y][x] = True 
    suma = 0
    ilosc = 0
    for pion, poziom in kierunki8:
        newx = x+poziom 
        newy = y+pion 
        try:
            suma += mapa[newy][newx]
            ilosc += 1
        except IndexError:
            pass
    mapa[y][x] = suma//ilosc
    for i in kierunki4:
        for pion, poziom in kierunki4:
            newx = x+poziom 
            newy = y+pion 
            try:
                if(odwiedzone[newy][newx] == True):
                    continue 
                kolejka.append((newy, newx))
            except IndexError:
                pass 

bok = 5
kolory = ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0,0) ]
krance = [(0, 4), (5, 20), (21, 45), (46, 80), (81, 100), (101, 120)]
for y in range(len(mapa)):
    turtle.goto(-200, -200+y*bok)
    for x in range(len(mapa[y])):
        kolor = 0
        for przedzial in range(6):
            if(mapa[y][x] >= krance[przedzial][0] and mapa[y][x] <= krance[przedzial][1]):
                kolor = kolory[przedzial]
        try:
            kwadrat(bok, kolor)
        except:
            print(kolor)
input()
    
