from turtle import penup, pendown, fd, lt, rt, setheading, goto, tracer, update
from random import randint
tracer(0,0)
ile_ramion = 9
kolumn_na_ramie = 50
lacznie_kolumn = kolumn_na_ramie * ile_ramion
kat_obrotu = 360/lacznie_kolumn

kolumny_wysokosci = []
for i in range(kolumn_na_ramie):
    kolumny_wysokosci.append(100+i*5)
#zaczynamy na srodku lewego ramienia
goto(0, 0)
lt(kat_obrotu/2)
for j in range(ile_ramion):
    for i in range(kolumn_na_ramie):
        fd(kolumny_wysokosci[i])
        lt(180)
        fd(kolumny_wysokosci[i])
        lt(180)
        rt(kat_obrotu)
update()
input()
