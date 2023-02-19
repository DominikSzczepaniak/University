# rysunek 4
#https://drive.google.com/drive/folders/1twa91wzrbuyFNY6k-oHg_Fe0BsTRQS2W 
#2019 zad 5
import turtle 
turtle.tracer(0, 1)
ilosc_kolumn = 17
ilosc_wierszy = 17
szerokosc = 20
for i in range(ilosc_wierszy+1):
    turtle.penup()
    turtle.goto(-200, -200+szerokosc*i)
    turtle.pendown()
    for j in range(ilosc_kolumn):
        turtle.fd(szerokosc)
turtle.lt(90)
for i in range(ilosc_kolumn+1):
    turtle.penup()
    turtle.goto(-200+szerokosc*i, -200)
    turtle.pendown()
    for j in range(ilosc_wierszy):
        turtle.fd(szerokosc)
turtle.update()
input()

