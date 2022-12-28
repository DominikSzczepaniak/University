from random import randint
import turtle 

def kwadrat(bok, kolor):
    turtle.fillcolor(kolor)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(bok)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(bok)
turtle.tracer(0,1)
turtle.colormode(255)
mapa = [[0]*100]*100
liczba_wylosowanych_pol = 50
for los in range(liczba_wylosowanych_pol):
    x = randint(0, 99)
    y = randint(0, 99)
    wysokosc = randint(0, 2139785789123)%255
    mapa[y][x] = wysokosc
procedura_wiele_razy = 700
kierunki = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, 1), (0,0)]
nowamapa = mapa
for los in range(procedura_wiele_razy):
    x = randint(0, 99)
    y = randint(0, 99)
    suma = 0
    ilosc = 0
    for pion, poziom in kierunki:
        newx = x+poziom 
        newy = y+pion 
        try:
            suma += mapa[newx][newy]
            ilosc += 1
        except IndexError:
            pass
    # print(suma, ilosc)
    nowamapa[y][x] = suma//ilosc
bok = 5
kolory = ['green', (127, 255, 0) , 'yellow', 'orange', 'red', (127, 0,0) ]
print(nowamapa)
for y in range(len(nowamapa)):
    turtle.goto(-200, -200+y*bok)
    for x in range(len(nowamapa[y])):
        kolor = kolory[int(int(nowamapa[y][x] // (255//6)))]
        print(kolor)
        kwadrat(bok, kolor)
input()
    
