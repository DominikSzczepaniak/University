from math import sin, pi
def f(x):
    return 2023*x**8 + 1977*x**7 - 1939*x**4 + 1410*x**2 - 966*x + 1996

xi = [-2023, 1977, -1945, sin(1), 1989, -1939, 1791, 1945, pi]
xi2 = [-1, 0, 1]
yi = [f(x) for x in xi]
yi2 = [f(x) for x in xi2]
print(yi2)
exit(0)
wspolczynniki = []
for i in range(len(xi)):
    dol = 1
    for j in range(len(xi)):
        if(i == j):
            continue
        dol *= xi[i] - xi[j]
    wspolczynniki.append(dol)
print(wspolczynniki)