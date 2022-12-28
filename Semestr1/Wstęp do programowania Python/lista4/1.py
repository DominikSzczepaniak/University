from turtle import *
import random
import numpy as np 
speed("fastest")
tracer(0,0) #usuniecie animacji turtle aby przyspieszyc rysunek
def kwadrat(bok, kolor): 
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        lt(90)
    end_fill()

def kwadratr(bok, kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()    

def slimak():
    licznik = 2
    bok = 20
    kolor1 = np.array([1,1,0])
    kolor2 = np.array([1, 0.07, 0.57])
    N = 18
    alfa_temp = 1/N
    mieszanka_temp = (1-alfa_temp) * kolor1 + alfa_temp * kolor2
    #dwa poczatkowe kwadraty
    kwadratr(bok, mieszanka_temp)
    fd(bok)
    kwadratr(bok, mieszanka_temp)
    rt(90)
    fd(bok)
    while(licznik < 19): #kazdy "poziom" slimaka
        for i in range(licznik): #kazdy kwadrat w poziomie
            alfa = licznik / N 
            mieszanka = (1-alfa) * kolor1 + alfa * kolor2
            kwadrat(bok, mieszanka)
            if(i != licznik-1): 
                fd(bok)
        rt(90)
        licznik += 1
    update() #pokazanie rysunku
    input()

slimak()

