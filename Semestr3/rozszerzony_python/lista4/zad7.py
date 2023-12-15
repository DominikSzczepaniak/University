def poprawne_pole(y, x, plansza, liczba):
    if(plansza[y][x] != 0):
        return False
    for i in range(9):
        if plansza[y][i] == liczba:
            return False
    for i in range(9):
        if plansza[i][x] == liczba:
            return False
    kwadrat_x = (x // 3) * 3
    kwadrat_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if plansza[kwadrat_y + i][kwadrat_x + j] == liczba:
                return False
    return True

def znajdz_puste(plansza):
    for i in range(9):
        for j in range(9):
            if plansza[i][j] == 0:
                return (i, j)
    return None

def rozwiaz(plansza):
    znajdz = znajdz_puste(plansza)
    if not znajdz:
        yield [row[:] for row in plansza]
        return
    rzad, kolumna = znajdz
    for num in range(1, 10):
        if(poprawne_pole(rzad, kolumna, plansza, num)):
            plansza[rzad][kolumna] = num 
            yield from rozwiaz(plansza)
            plansza[rzad][kolumna] = 0
    return 0

def rozwiazania(plansza):
    plansza = plansza.split('\n')
    plansza = [[int(i) for i in row] for row in plansza]
    for rozwiazanie in rozwiaz(plansza):
        yield rozwiazanie

def wypisywanie_planszy(plansza):
    for i in plansza:
        for j in i:
            print(j, end=' ')
        print()


plansza = """123456789
456789123
789123456
231978000
564312000
897564000
312800000
645200000
978600000"""
licznik = 0
for rozwiazanie in rozwiazania(plansza):
    licznik += 1
    print("Rozwiazanie %s:" % licznik)
    wypisywanie_planszy(rozwiazanie)