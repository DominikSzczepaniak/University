#0.5 pkt - napisanie funkcji losujaca z przedzialu [0, nieskonczonosci] z naturalnych
#znalezc liczbe y z przedzialu (0, 1], wylosowana = 1/y
#
import random
from math import floor 
def liczba_losowa_naturalna(k):
    x = random.random()
    y = 1 - x
    z = floor(k*(1/y) - 1)
    print(z)
k = random.randint(1, 10**8)
liczba_losowa_naturalna(random.randint(1, 10**8))