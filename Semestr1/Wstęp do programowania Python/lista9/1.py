from turtle import *

tracer(0)
# speed("fastest")

def dywan(punkt_startowy, bok, glebokosc):
    bok /= 3
    glebokosc -= 1
    penup()
    goto(punkt_startowy[0] - bok / 2, punkt_startowy[1] + bok / 2) #x chce isc w lewo, y w gore
    pendown()
    begin_fill()
    for i in range(4):
        forward(bok)
        right(90)
    end_fill()
    if glebokosc:
        x, y = punkt_startowy
        # [(x+k*bok,y+l*bok) for k,l in zip([-1,0,1],[-1,0,1]) if (k,l)==(0,0)]
        dywan((x - bok, y + bok), bok, glebokosc) #lewy gorny
        dywan((x, y + bok), bok, glebokosc) #gora srodek
        dywan((x + bok, y + bok), bok, glebokosc) #prawy gorny
        dywan((x - bok, y), bok, glebokosc) #lewy srodek
        dywan((x + bok, y), bok, glebokosc) #prawy srodek
        dywan((x - bok, y - bok), bok, glebokosc) #lewy dolny
        dywan((x, y - bok), bok, glebokosc) #dol srodek
        dywan((x + bok, y - bok), bok, glebokosc) #prawy dolny

dywan((0, 0), 600, 5)
# update()
done()