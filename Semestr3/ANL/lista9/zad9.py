from math import factorial
from matplotlib import pyplot as plt
punkty_kontrolne = [(0, 0), (3.5, 36), (25, 25), (25, 1.5), (-5, 3), (-5, 33), (15, 11), (-0.5, 35), (19.5, 15.5), (7, 0), (1.5, 10.5)]
wagi = [1,6,4,2,3,4,2,1,5,4,1]
wagi2 = [6, 1, 6, 1, 6, 1, 6,1, 6, 1, 6]
wagi3 = [1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1]
wagi4 = [1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11]

def bernstein(n, i, t):
    return (factorial(n)/(factorial(i)*factorial(n-i)))*(t**i)*((1-t)**(n-i))

def Rn(n, t, wagi):
    gora = 0
    for i in range(0, n+1):
        gora += wagi[i]*punkty_kontrolne[i][0]*bernstein(n, i, t)
    dol = 0 
    for i in range(0, n+1):
        dol += wagi[i]*bernstein(n, i, t)
    return gora/dol

def Sn(n, t, wagi):
    gora = 0
    for i in range(0, n+1):
        gora += wagi[i]*punkty_kontrolne[i][1]*bernstein(n, i, t)
    dol = 0 
    for i in range(0, n+1):
        dol += wagi[i]*bernstein(n, i, t)
    return gora/dol

def R(t, wagi):
    return Rn(10, t, wagi)

def S(t, wagi):
    return Sn(10, t, wagi)

def main(wagi):
    t = [i/100 for i in range(0, 101)]
    x = [R(i, wagi) for i in t]
    y = [S(i, wagi) for i in t]
    plt.plot(x, y)
    plt.show()

main(wagi)
main(wagi2)
main(wagi3)
main(wagi4)
#przedstawia litere B