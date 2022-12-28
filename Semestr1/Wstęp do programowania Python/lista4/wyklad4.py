import random
from turtle import *
import numpy as np
speed('fastest')
def move(x, y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(x, y, bok, kolor):
    move(x,y)
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()
def gradient():
    kolor1 = np.array([1,1,0.5])
    kolor2 = np.array([0.1, 0.1, 1])
    N = 20
    bok = 25
    for i in range(N+1):
        alfa = i / N 
        mieszanka = (1-alfa) * kolor1 + alfa * kolor2
        kwadrat(-200+bok*i,0, bok, mieszanka)
    input()

def krzywa_koch():
    def koch(poziom, dlugosc):
        if(poziom==0):
            fd(dlugosc)
        else:
            dlugosc_nowa = dlugosc / 3
            koch(poziom-1, dlugosc_nowa)
            lt(60)
            koch(poziom-1, dlugosc_nowa)
            rt(120)
            koch(poziom-1, dlugosc_nowa)
            lt(60)
            koch(poziom-1, dlugosc_nowa)
    for i in range(3):
        koch(3, 300)
        rt(120)

def duplikaty():
    def usun_duplikaty1(L):
        wynik = []
        for e in L:
            if e not in wynik:
                wynik.append(e)
        return wynik 

    def usun_duplikaty2(L):
        wynik = []
        zbior = set()
        for e in L:
            if e not in zbior:
                wynik.append(e)
                zbior.add(e)
        return wynik
    N = 7
    # nowy = usun_duplikaty1( list(range(10 ** N)) )
    nowy = usun_duplikaty2( list(range(10 ** N)) )
    print(len(nowy))


def czytanie():
    plik = open('popularne_slowa.txt', 'r') #'r' - czytanie, mozna moniac 'rb' - czytanie binarnego tekstu
    tekst = plik.read().split()
    print(tekst[:10])
