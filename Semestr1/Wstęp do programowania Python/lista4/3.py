from random import randint, choice

def randperm(n):
    wynik = [i for i in range(n)]
    for i in range(n):
        pozycja = randint(i, n-1) #bierzemy dowolna liczbe do zamiany miejscami z obecna pozycja i pozycja wylosowana
        wynik[i], wynik[pozycja] = wynik[pozycja], wynik[i]
        # pamiec = wynik[i]
        # wynik[i] = wynik[pozycja] 
        # wynik[pozycja] = pamiec
    return wynik
print(randperm(9))
print(randperm(9))
print(randperm(9))
print(randperm(10**6))
