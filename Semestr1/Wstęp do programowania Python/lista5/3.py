import duze_cyfry
from turtle import *
from random import randint
speed("fastest")
tracer(0,0)
def kwadrat(bok, kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

def rysuj_cyfre(n, bok, ktora_cyfra, kolor):
    penup()
    goto(-200+bok*6*ktora_cyfra, 0)
    pendown()
    cyfra = duze_cyfry.daj_cyfre(n)
    poziom = 0
    for i in cyfra:
        for j in i:
            if(j == "#"):
                kwadrat(bok, kolor)
                penup()
                fd(bok)
                pendown()
            else:
                penup()
                fd(bok)
                pendown()
        penup()
        poziom += 1
        goto(-200+bok*6*ktora_cyfra, -1 * bok * poziom)
        pendown()

def rysuj_liczbe(n, bok):
    licznik = 0
    for s in str(n):
        id1 = randint(0, 100) / 100
        id2 = randint(0, 100) / 100
        id3 = randint(0, 100) / 100
        kolor = [id1, id2, id3]
        rysuj_cyfre(int(s), bok, licznik, kolor)
        licznik+=1
    update()
    input()
        
n = int(input("Wpisz liczbe do narysowania: "))
rysuj_liczbe(n, 15)



