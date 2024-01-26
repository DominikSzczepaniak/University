#lagrange polynomial interpolation
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
points = open("punkty.csv", "r")
points = points.readlines()
points = [point.strip().split(",") for point in points]
points = [(float(point[0]), float(point[1])) for point in points]
xs = [point[0] for point in points]
ys = [point[1] for point in points]
def podpunkta():
    def f(t):
        return (t-1.2)*(t+4.7)*(t-2.3)
    #plot function for points[0] and plot points on it
    x = np.linspace(-5, 5, 1000)
    y = f(x)
    plt.plot(x, y, label='f(t)')
    plt.scatter(*zip(*points), color='red', label='Data points')
    plt.legend()
    plt.show()

# podpunkta()

def podpunktb(points=points):
    def lagrange_interpolation(x, y, x_interp):
        n = len(x)
        y_interp = np.zeros_like(x_interp, dtype=float)

        for i in range(n):
            term = y[i]
            for j in range(n):
                if j != i:
                    term *= (x_interp - x[j]) / (x[i] - x[j])
            y_interp += term

        return y_interp


    x_interp = np.linspace(min(xs), max(xs), 1000)

    y_interp = lagrange_interpolation(xs, ys, x_interp)

    plt.scatter(xs, ys, label='Punkty danych')
    plt.plot(x_interp, y_interp, label='Interpolacja Lagrange\'a', color='red')
    plt.legend()
    plt.title('Interpolacja Lagrange\'a')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#podpunktb()

def podpunktc(x, n, points=points):
    w = [0 for _ in range(16)]
    Pprim = [0 for _ in range(len(points))]
    P = [[0 for _ in range(len(points))] for _ in range(16)]
    a = []
    c = [0]
    d = [0, 0]
    iskal = []
    Pprim[0] = 1
    suma_y = 0
    for i in range(len(points)):
        suma_y += points[i][1]
        P[0][i] = 1
    a.append(suma_y/len(points))
    w[0] = a[0]
    iskal.append(len(points)) 
    #P_1(x) tutaj:
    c_1 = 0
    iloczyn_skalarny = len(points) #iloczyn skalarny dla P_0 czyli po prostu dlugosc - dobrze
    for i in range(len(points)):
        c_1 += points[i][0] #kazdy punkt zsumowany - dobrze
    c_1 = c_1 / iloczyn_skalarny #dzielimy przez iloczyn skalarny - dobrze
    c.append(c_1) 
    gora = 0
    
    for i in range(len(points)): #faza liczenia wartosci a
        P[1][i] = (points[i][0] - c_1)
        gora += points[i][1]*P[1][i] #f(xi) * P_k(x_i) = f(x_i) * P_1(x_i) - dobrze
    
    iloczyn_skalarny = 0
    for i in range(len(points)):
        iloczyn_skalarny += P[1][i] ** 2 
    iskal.append(iloczyn_skalarny)
    dol = iskal[1]
    a.append(gora/dol) #dodajemy a - dobrze
    Pprim[1] = (x - c_1) #wartosc P_1(x) = (x-c_1) - dobrze
    w[1] = a[1] * Pprim[1] #w - wartosc a * P_1(wejsciowy x) - dobrze

    #------------------------------------------------------------------------------------------------

    #P_k(x) tutaj:
    for k in range(2, 16):
        c_k = 0
        for i in range(len(points)):
            c_k += points[i][0] * P[k-1][i]*P[k-1][i] # dobrze
        c_k = c_k / iskal[k-1] #dobrze
        c.append(c_k) #dobrze
        d_k = iskal[k-1]/iskal[k-2] #iloczyn skalarny poprzedniego / przedpoprzedniego - dobrze
        d.append(d_k)

        gora = 0
        
        iloczyn_skalarny = 0
        for i in range(len(points)):
            #P_k(x) = (xk-c) * P[k-1][i] - d_2 * P[k-2][i]
            #gora a = f(xi) * P_k(xi)
            P[k][i] = ((points[i][0] - c_k) * P[k-1][i] - (d_k * P[k-2][i]))
            gora += points[i][1] * P[k][i] 
            #dobrze
            iloczyn_skalarny += P[k][i] ** 2

        iskal.append(iloczyn_skalarny)
        dol = iskal[k] #iloczyn skalarny dla obecnego p - czyli to co liczylismy calkiem niedawno
        a.append(gora/dol)
        Pprim[k] = (x - c_k)*Pprim[k-1] - (d_k * Pprim[k-2]) #dobrze
        w[k] = a[k] * Pprim[k]

    for i in range(1, len(w)):
        w[i] = w[i] + w[i-1]
    return w[n]
    

def wyswietl_dla_n(n):
    punkty_do_wywolania = [i[0] for i in points]
    x_y = []
    y_y = []
    for i in punkty_do_wywolania:
        wynik = podpunktc(i, n) 
        x_y.append(i)
        y_y.append(wynik)
    plt.plot(x_y, y_y, marker='o', linestyle='None')
    plt.title("Wielomian stopnia: " + str(n))
    plt.scatter(*zip(*points), color='red', label='Data points')
    plt.show()

# for i in range(1, 6):
#     wyswietl_dla_n(i)
