from time import localtime
from turtle import *
tracer(0,1)
czas = localtime()
godzina, minuta = czas[3], czas[4]
width(2)
def pusta_tarcza():
    kat = 6
    for i in range(12):
        #start od godzinowej 
        penup()
        fd(300)
        pendown()
        width(5)
        fd(20)
        penup()
        backward(320)
        rt(kat)
        for j in range(4):
            penup()
            fd(300)
            pendown()
            width(2)
            fd(10)
            penup()
            backward(310)
            rt(kat)
    
def zegar(godzina, minuta):
    kat = 6
    for i in range(12):
        #start od godzinowej 
        penup()
        fd(300)
        pendown()
        width(5)
        fd(20)
        penup()
        backward(320)
        rt(kat)
        for j in range(4):
            penup()
            fd(300)
            pendown()
            width(2)
            fd(10)
            penup()
            backward(310)
            rt(kat)
    pendown()
    lt(90)
    kat_godzinowej = (godzina%12)%12*30+(30*minuta/60)
    kat_minutowej = 360*minuta/60
    width(5)
    rt(kat_godzinowej)
    fd(150)
    backward(150)
    lt(kat_godzinowej)
    rt(kat_minutowej)
    width(5)
    fd(200)
    backward(200)
    update()
    input()

zegar(godzina, minuta)
