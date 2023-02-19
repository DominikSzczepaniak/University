#rysowanie mapy z szesciokatow, z szesciokatami o roznych kolorach w srodku szesciokatow tworzacych mape
import turtle
from math import sqrt
from random import choice
turtle.tracer(0, 1)
# turtle.speed("fastest")
def szesciokat(a, kolorowac= False):
    kat = 60 
    if(kolorowac == True):
        kolor = choice(["red", "blue", "black", "brown", "yellow", "orange", "green", "purple"])
        turtle.fillcolor(kolor)
        turtle.begin_fill()
    turtle.lt(60)
    for i in range(6):
        turtle.fd(a)
        turtle.rt(kat)
    if(kolorowac==True):
        turtle.end_fill()

def rysuj_mape():
    bok = 10
    bok_mniejszy = 8
    roznica = (bok-bok_mniejszy)/2
    print(roznica)
    ilosc_kolumn_podwojnych = 20
    wysokosc_kolumny = 20
    for i in range(ilosc_kolumn_podwojnych):
        if(i%2==0):
            turtle.penup()
            turtle.goto(-100+bok*i*1.5, -100)
            if(i!=0):
                turtle.rt(60)
            turtle.pendown()
        else:
            turtle.penup()
            turtle.goto(-100+bok*i*1.5, -100+bok)
            if(i != 0):
                turtle.rt(60)
            turtle.pendown()
        for wys in range(wysokosc_kolumny):
            start_miejsce = turtle.position()
            szesciokat(bok)
            zapisz_miejsce = turtle.position()
            if(wys != wysokosc_kolumny-1):
                turtle.penup()
                turtle.fd(bok)
                turtle.lt(60)
                turtle.fd(bok)
                turtle.rt(120)
                turtle.pendown()
                zapisz_miejsce = turtle.position()
            turtle.penup()
            turtle.goto(start_miejsce)
            turtle.fd(roznica)
            turtle.pendown()
            if(wys == wysokosc_kolumny-1):
            #     turtle.penup()
            #     turtle.lt(60)
            #     turtle.fd(bok)
                turtle.rt(60)
                turtle.fd(roznica)
                # turtle.pendown()
            szesciokat(bok_mniejszy, True)
            if(wys == wysokosc_kolumny -1):
                turtle.lt(60)
            turtle.penup()
            try:
                turtle.goto(zapisz_miejsce)
            except:
                pass
            turtle.pendown()
            turtle.rt(60)
            turtle.update()


rysuj_mape()
input()

