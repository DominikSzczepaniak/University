def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nowy_ulamek(num, denom):
    gcd = nwd(num, denom)
    num //= gcd
    denom //= gcd

    return [num, denom]

def show(u):
    print(f"{u[0]}/{u[1]}")

def dodaj(u1, u2):
    num = u1[0] * u2[1] + u2[0] * u1[1]
    denom = u1[1] * u2[1]
    return nowy_ulamek(num, denom)

def dodaj2(u1, u2):
    w = u2[1]
    u2[1] *= u1[1]
    u2[0] *= u1[1]
    u1[1] *= w
    u1[0] *= w
    u2 = nowy_ulamek(u1[0] + u2[0], u1[1])

def odejmij(u1, u2):
    num = u1[0] * u2[1] - u2[0] * u1[1]
    denom = u1[1] * u2[1]
    return nowy_ulamek(num, denom)

def odejmij2(u1, u2):
    w = u2[1]
    u2[1] *= u1[1]
    u2[0] *= u1[1]
    u1[1] *= w
    u1[0] *= w
    u2 = nowy_ulamek(u1[0] - u2[0], u1[1])

def pomnoz(u1, u2):
    num = u1[0] * u2[0]
    denom = u1[1] * u2[1]
    return nowy_ulamek(num, denom)

def pomnoz2(u1, u2):
    u2 = nowy_ulamek(u1[0]*u2[0], u1[1]*u2[1])

def podziel(u1, u2):
    num = u1[0] * u2[1]
    denom = u1[1] * u2[0]
    return nowy_ulamek(num, denom)

def podziel2(u1, u2):
    u2[1], u2[0] = u2[0], u2[1]
    u2 = pomnoz(u1, u2)

ulamek1 = nowy_ulamek(1, 2)
ulamek2 = nowy_ulamek(3, 4)

show(ulamek1)
show(ulamek2)
print()

wynik_dodawania = dodaj(ulamek1, ulamek2)
show(wynik_dodawania)
print()

wynik_odejmowania = odejmij(ulamek1, ulamek2)
show(wynik_odejmowania)
print()

wynik_mnozenia = pomnoz(ulamek1, ulamek2)
show(wynik_mnozenia)
print()

wynik_dzielenia = podziel(ulamek1, ulamek2)
show(wynik_dzielenia)
print()

show(ulamek1)
show(ulamek2)
dodaj2(ulamek1, ulamek2)
print()
show(ulamek1)
show(ulamek2)
odejmij2(ulamek1, ulamek2)
print()
show(ulamek1)
show(ulamek2)
pomnoz2(ulamek1, ulamek2)
print()
show(ulamek1)
show(ulamek2)
podziel2(ulamek1, ulamek2)
print()

