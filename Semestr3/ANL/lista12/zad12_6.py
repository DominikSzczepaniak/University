import numpy as np
import math
a = -1
b = 1
def f(x):
    return 1/(1+25*x**2)

MAX_N = 25
W = np.zeros((MAX_N, MAX_N))
started = np.zeros((MAX_N))
obliczone = np.zeros((MAX_N))

silnie = [1, 1]
for i in range(2, MAX_N+5):
    silnie.append(silnie[-1]*i)

def obliczWspolczynniki(n): #liczy bardzo dobrze, tu nie ma bledu
    global W

    x = n
    #robimy tablice W n+1 x n+1 gdzie kolumny to (t-i) ktore jest pomijane
    #a wiersze to wspolczynniki wielomianu 
    #W[0][0] da nam wspolczynnik przy t^0 dla wielomianu (t-1)(t-2)...(t-n)
    for i in range(MAX_N): #i to kolumna ktora jest ignorowana
        if(x == i): #jesli x == i to pomijamy 
            continue
        if(started[i] == 0): #jesli x == 0 to mamy (t-i)
            W[i][1] = 1
            W[i][0] = -x
            started[i] = 1
            continue
        noweW = np.zeros(MAX_N) #nowe wspolczynniki ktore stworzy nam mnozenie wszystkich poprzednich przez t
        noweW2 = np.zeros(MAX_N)
        for j in range(MAX_N):
            if(j != MAX_N-1):
                noweW[j+1] += W[i][j] #to sa wspolczynniki ktore dodalo t - zwiekszamy stopien wszystkich wspolczynnikow o 1
            noweW2[j] += W[i][j]*(-x) #to sa wspolczynniki ktore dodalo -x - jesli mielismy 3t^2 to teraz mamy -3xt^2 + t*t^1, wiec musimy dodac
        for j in range(MAX_N):
            W[i][j] = noweW[j] + noweW2[j] #dodajemy do siebie nowe wspolczynniki oraz te ktore utworzylismy
        W[i][MAX_N-1] = 1
    
    return W

def newton_cotes(n):
    A = []
    h = (b-a)/n
    # print(n, h)
    for i in range(n+1):
        if(obliczone[i] == 0):
            obliczWspolczynniki(i)
            obliczone[i] = 1
    for k in range(math.ceil((n+1)/2)):
        # print(k)
        wspolczynniki = W[k]
        #print(wspolczynniki) #dobrze sa
        P = 1 #wartosc przed znakiem calki
        if((n - k) % 2 == 1):
            gora = -1 * h 
            dol = (silnie[k] * silnie[n-k]) 
            # print("k, gora, dol: ", k, gora, dol)
            P = (-1 * h) / (silnie[k] * silnie[n-k])
        else:
            P = (1 * h) / (silnie[k] * silnie[n-k])
        # print(P)
        calka = 0
        for i in range(n+1):
            wspolczynnik = wspolczynniki[i]
            stopien = i 
            calka += wspolczynnik * (n**(stopien+1)) / (stopien+1)
        # print(calka)
        A.append(P * calka)
    if(n%2==1):
        for i in range(len(A)-1, -1, -1):
            A.append(A[i])
    else:
        for i in range(len(A)-2, -1, -1):
            A.append(A[i])
    # print(A) #oblicza poprawnie
    wynik = 0
    # print(h)
    for i in range(n+1):
        # print(a+i*h)
        # print(A[i], f(a + i*h))
        # print(A[i] * f(a + i*h))
        wynik += A[i] * f(a + i*h)
    return wynik 


for i in range(2, MAX_N):
    print("n = ", i, " ", newton_cotes(i))

#niestety ale wyniki nie sa ani troche poprawne.
#najblizej poprawnego jest wynik dla n = 7.
#zakladam, ze dla wiekszych n problemem staja sie bledy numeryczne przy dzieleniu przez bardzo duza silnie

# print(newton_cotes(8))
#dla n=8 mamy:
    #A0: https://www.wolframalpha.com/input?i2d=true&i=Divide%5BPower%5B%5C%2840%29-1%5C%2841%29%2C8-0%5D*%5C%2840%29Divide%5B2%2C8%5D%5C%2841%29%2C0%21*%5C%2840%298-0%5C%2841%29%21%5D*Integrate%5B%5C%2840%29t-1%5C%2841%29%5C%2840%29t-2%5C%2841%29%5C%2840%29t-3%5C%2841%29%5C%2840%29t-4%5C%2841%29%5C%2840%29t-5%5C%2841%29%5C%2840%29t-6%5C%2841%29%5C%2840%29t-7%5C%2841%29%5C%2840%29t-8%5C%2841%29%2C%7Bt%2C0%2C8%7D%5D
    #A1: https://www.wolframalpha.com/input?i2d=true&i=Divide%5BPower%5B%5C%2840%29-1%5C%2841%29%2C8-1%5D*%5C%2840%29Divide%5B2%2C8%5D%5C%2841%29%2C1%21*%5C%2840%298-1%5C%2841%29%21%5D*Integrate%5B%5C%2840%29t-0%5C%2841%29%5C%2840%29t-2%5C%2841%29%5C%2840%29t-3%5C%2841%29%5C%2840%29t-4%5C%2841%29%5C%2840%29t-5%5C%2841%29%5C%2840%29t-6%5C%2841%29%5C%2840%29t-7%5C%2841%29%5C%2840%29t-8%5C%2841%29%2C%7Bt%2C0%2C8%7D%5D
    #A2: https://www.wolframalpha.com/input?i2d=true&i=Divide%5BPower%5B%5C%2840%29-1%5C%2841%29%2C8-2%5D*%5C%2840%29Divide%5B2%2C8%5D%5C%2841%29%2C2%21*%5C%2840%298-2%5C%2841%29%21%5D*Integrate%5B%5C%2840%29t-0%5C%2841%29%5C%2840%29t-1%5C%2841%29%5C%2840%29t-3%5C%2841%29%5C%2840%29t-4%5C%2841%29%5C%2840%29t-5%5C%2841%29%5C%2840%29t-6%5C%2841%29%5C%2840%29t-7%5C%2841%29%5C%2840%29t-8%5C%2841%29%2C%7Bt%2C0%2C8%7D%5D
    #A3: https://www.wolframalpha.com/input?i2d=true&i=Divide%5BPower%5B%5C%2840%29-1%5C%2841%29%2C8-3%5D*%5C%2840%29Divide%5B2%2C8%5D%5C%2841%29%2C3%21*%5C%2840%298-3%5C%2841%29%21%5D*Integrate%5B%5C%2840%29t-0%5C%2841%29%5C%2840%29t-1%5C%2841%29%5C%2840%29t-2%5C%2841%29%5C%2840%29t-4%5C%2841%29%5C%2840%29t-5%5C%2841%29%5C%2840%29t-6%5C%2841%29%5C%2840%29t-7%5C%2841%29%5C%2840%29t-8%5C%2841%29%2C%7Bt%2C0%2C8%7D%5D
    #A4: https://www.wolframalpha.com/input?i2d=true&i=Divide%5BPower%5B%5C%2840%29-1%5C%2841%29%2C8-4%5D*%5C%2840%29Divide%5B2%2C8%5D%5C%2841%29%2C4%21*%5C%2840%298-4%5C%2841%29%21%5D*Integrate%5B%5C%2840%29t-0%5C%2841%29%5C%2840%29t-1%5C%2841%29%5C%2840%29t-2%5C%2841%29%5C%2840%29t-3%5C%2841%29%5C%2840%29t-5%5C%2841%29%5C%2840%29t-6%5C%2841%29%5C%2840%29t-7%5C%2841%29%5C%2840%29t-8%5C%2841%29%2C%7Bt%2C0%2C8%7D%5D