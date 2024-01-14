import numpy as np
a = -1
b = 1
def f(x):
    return 1/(1+25*x**2)

silnie = [1]
for i in range(2, 30):
    silnie.append(silnie[-1]*i)


W = np.zeros((26, 26))


def binomial(n, k):
    return silnie[n] / (silnie[k]*silnie[n-k])
def obliczWspolczynniki(n): #liczy bardzo dobrze, tu nie ma bledu
    global W
    x = n
    #robimy tablice W n+1 x n+1 gdzie kolumny to (t-i) ktore jest pomijane
    #a wiersze to wspolczynniki wielomianu 
    #W[0][0] da nam wspolczynnik przy t^0 dla wielomianu (t-1)(t-2)...(t-n)
    for i in range(n+1): #i to kolumna ktora jest ignorowana
        started = False
        for x in range(n+1): 
            if(x == i): #jesli x == i to pomijamy 
                continue
            if(started == False): #jesli x == 0 to mamy (t-i)
                W[i][1] = 1
                W[i][0] = -x
                started = True
                continue
            noweW = np.zeros(n+1) #nowe wspolczynniki ktore stworzy nam mnozenie wszystkich poprzednich przez t
            noweW2 = np.zeros(n+1)
            for j in range(n):
                noweW[j+1] += W[i][j] #to sa wspolczynniki ktore dodalo t - zwiekszamy stopien wszystkich wspolczynnikow o 1
                noweW2[j] += W[i][j]*(-x) #to sa wspolczynniki ktore dodalo -x - jesli mielismy 3t^2 to teraz mamy -3xt^2 + t*t^1, wiec musimy dodac
            for j in range(n):
                W[i][j] = noweW[j] + noweW2[j] #dodajemy do siebie nowe wspolczynniki oraz te ktore utworzylismy
            W[i][n] = 1
    return W

test = obliczWspolczynniki(3)[0]
print(test)

# def newton_cotes(n):
#     A = []
#     h = (b-a)/n
#     for k in range(n+1):
#         wspolczynniki = obliczWspolczynniki(n, n)[k]
#         P = 1 #wartosc przed znakiem calki
#         if(n - k % 2 == 1):
#             P = (-1 * h) / (silnie[k] * silnie[n-k])
#         else:
#             P = (-1 * h) / (silnie[k] * silnie[n-k])
#         calka = 0
#         for i in range(n+1):
#             wspolczynnik = wspolczynniki[i]
#             stopien = i 
#             calka += wspolczynnik * (n**(stopien+1)) / (stopien+1)
#         # print(calka)
#         A.append(P * calka)

#     wynik = 0
#     for i in range(n+1):
#         # print(a+i*h)
#         wynik += A[i] * f(a + i*h)
#     return wynik 


# for i in range(2, 25):
#     print("n = ", i, " ", newton_cotes(i))