import random
import math
srodek = (0.5, 0.5)
def losowanie():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    odleglosc = ((x - srodek[0])**2 + (y - srodek[1])**2)**0.5
    if odleglosc < 0.5:
        return True
    else:
        return False

def liczba_pi(n, roznica = 0):
    '''
    jesli roznica = 0 to konczymy po n losowaniach
    jesli n = 0 to konczymy losowanie dopiero po odpowiednim przyblizeniu'''
    if(n == 0 and roznica == 0):
        print("Nie podano warukow konca losowania")
        return 0
    trafienia = 0
    if(n==0):
        rzutow = 0
        while(True):
            rzutow += 1
            if losowanie():
                trafienia += 1
            wartosc = (4 * trafienia) / rzutow
            if abs(math.pi - wartosc) < roznica:
                print(wartosc)
                return wartosc
            print(wartosc)
    else:
        for i in range(n):
            if losowanie():
                trafienia += 1
            wartosc = (4 * trafienia) / (i+1)
            print(wartosc)
        return (4 * trafienia) / n
liczba_pi(0, 0.00000001)

#liczba_pi(10000000)
