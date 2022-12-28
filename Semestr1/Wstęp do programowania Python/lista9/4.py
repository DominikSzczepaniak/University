from turtle import *
from random import randint, shuffle
from time import sleep 
from kwadrat import kwadrat
plansza = """
...kkkkkkkkkkkk.......
......................
......................
......................
..nnnn................
..nnnn................
..n...................
......................
.........kkkkkkkkkkk..
......................
......................
......................
......................
.........ppppp........
......................
"""
tab = [list(wiersz) for wiersz in plansza.split()]
MY = len(tab)
MX = len(tab[0])
sily = [MX * [0] for i in range(MY)]
for i in range(len(sily)):
    for j in range(len(sily[0])):
        if(sily[i][j] != "."):
            sily[i][j] = randint(1, 5)
        else:
            sily[i][j] = 0
kierunki = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def isGrid(x, y, n, m):
    if(x >= 0 and x <n and y >= 0 and y < m):
        return True 
    return False 
def rysuj_plansze(tab):
    clear()
    for y in range(MY):
        for x in range(MX):
            if tab[y][x] == 'k':
                kolor = 'brown'
            elif tab[y][x] == 'n':
                kolor = 'grey'
            elif tab[y][x] == 'p':
                kolor = 'lightblue'
            else:
                kolor = 'white'
            kwadrat(x, y, kolor)
    update() 

while True:
    rysuj_plansze(tab)
    nowa = [ MX * ['.']  for y in range(MY)]
    nowe_sily = [ MX * [0]  for y in range(MY)]
    for x in range(MX):
        for y in range(MY):
            if(tab[y][x] == "."):
                continue
            nowa[y][x] = tab[y][x]
            nowe_sily[y][x] = sily[y][x]
            shuffle(kierunki)
            for chx, chy in kierunki:
                if(isGrid(x+chx, y+chy, MX, MY)):
                    pole = tab[y+chy][x+chx]
                    naszepole = tab[y][x]
                    if(pole=="."):
                        if(sily[y][x] > 1):
                            nowa[y+chy][x+chx] = tab[y][x]
                            nowe_sily[y+chy][x+chx] = sily[y][x] - 1
                    elif(pole == "k"):
                        if(naszepole == "p"):
                            nowe_sily[y][x] = min(nowe_sily[y][x]+1, 5)
                            if(sily[y+chy][x+chx] == 1):
                                nowe_sily[y+chy][x+chx] = 0
                                nowa[y+chy][x+chx] = "."
                            else:
                                nowe_sily[y+chy][x+chx] = sily[y+chy][x+chx] - 1
                        elif(naszepole == "n"):
                            nowe_sily[y+chy][x+chx] = min(nowe_sily[y+chy][x+chx]+1, 5)
                            if(sily[y][x] == 1):
                                nowe_sily[y][x] = 0
                                nowa[y][x] = "."
                            else:
                                nowe_sily[y][x] = sily[y][x] - 1
                    elif(pole == "p"):
                        if(naszepole == "k"):
                            nowe_sily[y+chy][x+chx] = min(nowe_sily[y+chy][x+chx]+1, 5)
                            if(sily[y][x] == 1):
                                nowe_sily[y][x] = 0
                                nowa[y][x] = "."
                            else:
                                nowe_sily[y][x] = sily[y][x] - 1
                        elif(naszepole == "n"):
                            nowe_sily[y][x] = min(nowe_sily[y][x]+1, 5)
                            if(sily[y+chy][x+chx] == 1):
                                nowe_sily[y+chy][x+chx] = 0
                                nowa[y+chy][x+chx] = "."
                            else:
                                nowe_sily[y+chy][x+chx] = sily[y+chy][x+chx] - 1
                    elif(pole == "n"):
                        if(naszepole == "p"):
                            nowe_sily[y+chy][x+chx] = min(nowe_sily[y+chy][x+chx]+1, 5)
                            if(sily[y][x] == 1):
                                nowe_sily[y][x] = 0
                                nowa[y][x] = "."
                            else:
                                nowe_sily[y][x] = sily[y][x] - 1
                        elif(naszepole == "k"):
                            nowe_sily[y][x] = min(nowe_sily[y][x]+1, 5)
                            if(sily[y+chy][x+chx] == 1):
                                nowe_sily[y+chy][x+chx] = 0
                                nowa[y+chy][x+chx] = "."
                            else:
                                nowe_sily[y+chy][x+chx] = sily[y+chy][x+chx] - 1
    if tab == nowa:
        break 
    tab = nowa
    sily = nowe_sily 
    sleep(0.05)

print("Koniec")
input()