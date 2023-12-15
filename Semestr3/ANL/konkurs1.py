import matplotlib.pyplot as plt 
# xy = [0, -0.03, 0, 0.01, 0.03, 0, 1]#, 0.83, 1.1]
# yy = [2, 1, 0, 0.5, 1, 2, -0.2]#, 2.2, 2.1]
xy = []
yy = []
dane = []
def zamien_na_odpowiednie():
    for line in open("dane.txt"):
        zmienna = 0
        lewa = ""
        prawa = ""
        for i in line:
            if i == " ":
                continue
            if i == ")":
                dane.append([int(lewa), int(prawa)*-1])
                lewa = ""
                prawa = ""
                continue
            elif i == "(":
                continue 
            elif i == ",":
                zmienna += 1
                zmienna %= 2
                continue
            if(zmienna == 0):
                lewa += i
            else:
                prawa += i
def dodaj_dane():
    for i in dane:
        xy.append(i[0])
        yy.append(i[1])

zamien_na_odpowiednie()
dodaj_dane()

def h(k, xy):
    return xy[k] - xy[k - 1]

def lambdak(k, xy):
    if k == 0:
        return 0
    return h(k, xy) / (h(k, xy) + h(k + 1, xy))

def iloraz_roznicowy(xs, ys):
    if len(xs) == 1:
        return ys[0]
    return (iloraz_roznicowy(xs[1:], ys[1:]) - iloraz_roznicowy(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

def dk(k, xs, ys):
    if k == 0:
        return 0
    return 6 * iloraz_roznicowy(xs[(k - 1):(k + 2)], ys[(k - 1):(k + 2)])

def m(xs, ys):
    n = len(xs) - 1
    q = [0 for _ in range(n)]                          
    u = [0 for _ in range(n)]
    l = [lambdak(k, xs) for k in range(n)]
    d = [dk(k, xs, ys) for k in range(n)]
    for i in range(1, n):
        p = l[i] * q[i - 1] + 2
        q[i] = (l[i] - 1) / p
        u[i] = (d[i] - l[i] * u[i - 1]) / p
    m = [0 for _ in range(n + 1)]
    m[n - 1] = u[n - 1]
    for i in range(n - 2, 0, -1):
        m[i] = u[i] + q[i] * m[i + 1]
    return m

def sk(xs, ys, ms, k):
    return lambda x: \
        ((ms[k - 1] * (xs[k] - x) ** 3) / 6 + (ms[k] * (x - xs[k - 1]) ** 3) / 6 + \
        (ys[k - 1] - (ms[k - 1] * h(k, xs) ** 2) / 6) * (xs[k] - x) + \
        (ys[k] - (ms[k] * h(k, xs) ** 2) / 6) * (x - xs[k - 1])) / h(k, xs)

def get_s(xs, ys):
    ms = m(xs, ys)
    def res(x):
        for i in range(1, len(xs)):
            if xs[i - 1] <= x < xs[i]:
                return sk(xs, ys, ms, i)(x)
    return res 

t = [k / len(xy) for k in range(len(xy))]
sx = get_s(t, xy)
sy = get_s(t, yy)

M = 1000
uu = [k / M for k in range(M)]

plt.plot([sx(u) for u in uu], [sy(u) for u in uu], "r-")
plt.show()