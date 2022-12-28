from turtle import pensize, bk, fd, rt, lt, penup, pendown, speed
from random import randint 
penup()
lt(90)
lt(90)
fd(300)
rt(90)
pendown()
speed("fastest")
def kolumna(a, b):
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    fd(a)
    rt(90)
    fd(b)
    rt(180)
    fd(b)
    penup()
    fd(5)
    pendown()
    lt(90)

tablica = []
for i in range(40): 
    wysokosc = randint(10, 300)
    szerokosc = 10 
    tablica.append([wysokosc, szerokosc])
tablica = sorted(tablica)

for i in range(40):
    kolumna(tablica[i][0], tablica[i][1])


input()

pensize(5)


