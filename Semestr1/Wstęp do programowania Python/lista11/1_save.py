#https://skos.ii.uni.wroc.pl/pluginfile.php/54369/mod_resource/content/1/c8.pdf zad 4
from random import randint
import turtle 
from collections import deque
def kwadrat(bok, kolor):
    turtle.fillcolor(kolor)
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
mapa = [[0 for i in range(100)] for j in range(100)]
# ile_wzgorz = randint(3, 5)
# wielkosci = []
# for i in range(ile_wzgorz):
#     wielkosci.append(randint(20, 40))
liczba_wylosowanych_pol = randint(1000, 2000) #liczba nie moze byc mala jak jest napisane w zadaniu, bo jezeli bedzie mala to niewazne jaka wartosc wzgorza sie ustawi, to jesli dookola jest 8 pol o wysokosci 0, to srednia wazona z tego jest rowna wysokosc/9, a skoro mamy tylko 6 skali kolorow to automatycznie wartosc wpada do najnizszej skali, wiec cala mapa jest zielona z tylko kilkami kropkami w ktorych mamy nasze poczatkowe wzgorza
byly = set()
id = []
for los in range(liczba_wylosowanych_pol):
    x = randint(0, 99)
    y = randint(0, 99)
    krotka = (y, x)
    if(krotka in byly):
        continue
    id.append(krotka)
    mapa[y][x] = 80
    byly.add(krotka)


procedura_wiele_razy = 100000
kierunki8 = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, 1), (0,0)]
kierunki4 = [(1, 0), (0, 1), (0, -1), (-1, 0)]
nowamapa = mapa.copy()
kolejka = deque()
odwiedzone = [[False for i in range(100)] for j in range(100)]
for i in id:
    odwiedzone[i[0]][i[1]] = True 
    for i in kierunki4:
        for pion, poziom in kierunki4:
            newx = x+poziom 
            newy = y+pion 
            try:
                kolejka.append((newy, newx))
            except IndexError:
                pass
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
            suma += nowamapa[newy][newx]
            ilosc += 1
        except IndexError:
            pass
    nowamapa[y][x] = suma//ilosc
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
        



# zmienione = 0
# while(koniec(nowamapa) == False):
#     x = randint(0, 99)
#     y = randint(0, 99)
#     if(zmienione == 1500):
#         break
#     if((y, x) in byly):
#         continue
#     if(nowamapa[y][x] > 0):
#         zmienione += 1
#         byly.add((y, x))
#         continue
#     suma = 0
#     ilosc = 0
#     for pion, poziom in kierunki8:
#         newx = x+poziom 
#         newy = y+pion 
#         try:
#             suma += nowamapa[newy][newx]
#             ilosc += 1
#         except IndexError:
            # pass
    # nowamapa[y][x] = suma//ilosc
bok = 5
kolory = ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0,0) ]
for y in range(len(nowamapa)):
    turtle.goto(-200, -200+y*bok)
    for x in range(len(nowamapa[y])):
        kolor = kolory[ int((nowamapa[y][x]//(14))) ]
        kwadrat(bok, kolor)
input()
    
