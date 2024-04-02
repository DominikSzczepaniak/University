#jak ktos chce sciagnac sobie to zadanie, to nie polecam robic tego tym walksatem, to za chuja nie działa i nie warto sie z tym kurestwem meczyc
#zrob sobie to z algorytmem ac3 i sie nie mecz z tym gownem, nie warto

import random
import numpy as np
from itertools import combinations
from functools import cache
napisyWiersze = []
napisyKolumny = []
napisy = []
cacheWiersze = {}
cacheKolumny = {}
def generuj2(dl, liczby):
    global napisy
    if(sum(liczby) + len(liczby) - 1 == dl):
        napis = ""
        for i in range(len(liczby)):
            napis += "1" * liczby[i] 
            if(i != len(liczby)-1):
                napis += "0"
        napisy.append(napis)
        return

    def rekurencja(dl, liczby, miejsca_startowe):
        kolejna_zaczyna_sie = 0
        if(len(miejsca_startowe) != 0):
            kolejna_zaczyna_sie = miejsca_startowe[-1] + liczby[len(miejsca_startowe)-1] + 1 
        potrzebne_miejsca_dla_reszty = sum(liczby[len(miejsca_startowe):]) + len(liczby) - len(miejsca_startowe) - 2
        if(dl - kolejna_zaczyna_sie < potrzebne_miejsca_dla_reszty):
            return
        if(len(liczby) == len(miejsca_startowe)):
            miejsce = 0 
            napis = ""
            for i in range(len(miejsca_startowe)):
                napis += "0" * (miejsca_startowe[i] - miejsce) + "1" * liczby[i]
                miejsce = miejsca_startowe[i] + liczby[i]
            napis += "0" * (dl-len(napis))
            # print("dlugosc napisu: ", len(napis))
            if(len(napis) > dl):
                return
            napisy.append(napis)
            return
        for i in range(kolejna_zaczyna_sie, dl - potrzebne_miejsca_dla_reszty + 1):
            rekurencja(dl, liczby, miejsca_startowe + [i])
    for i in range(dl - sum(liczby) - len(liczby)+2):
        rekurencja(dl, liczby, [i])

def opt_dist_col(napis, nrKolumny): 
    lista = tuple(napis.tolist())
    if(lista in cacheKolumny):
        return cacheKolumny[lista]
    if type(napis) is not str:
        napis = "".join(map(str, napis))
    min_wynik = len(napis)+5
    for i in napisyKolumny[nrKolumny]:
        wynik = 0
        for j in range(len(napis)):
            if(i[j] != napis[j]):
                wynik += 1
        min_wynik = min(min_wynik, wynik)
    cacheKolumny[lista] = min_wynik
    return min_wynik

def opt_dist_row(napis, nrWiersza):
    lista = tuple(napis.tolist())
    if(lista in cacheWiersze):
        return cacheWiersze[lista]
    if type(napis) is not str:
        napis = "".join(map(str, napis))
    min_wynik = len(napis)+5
    for i in napisyWiersze[nrWiersza]:
        wynik = 0
        for j in range(len(napis)):
            if(i[j] != napis[j]):
                wynik += 1
        min_wynik = min(min_wynik, wynik)
    cacheWiersze[lista] = min_wynik
    return min_wynik


class nonogram():
    def __init__(self, n, m, rows, columns):
        self.n = n
        self.m = m
        self.rows = rows
        self.columns = columns
        self.coloring = np.random.randint(2, size=(n, m))
        # self.depth = min((n + m) * 500, 13000)
        self.depth = (n+m)*500
        # self.depth = 30*m*n
        self.dobreWiersze = set()
        self.dobreKolumny = set()
        self.dozwoloneWiersze = []
        self.dozwoloneKolumny = []
        self.resets = 0
        # self.start_pos = np.random.randint(2, size=(n, m))
        self.start_pos = np.zeros((n, m), dtype=int)
        self.visited = set()

        self.INSTANT_NAPRAWA_WIERSZ = m #m - off
        self.INSTANT_NAPRAWA_KOLUMNA = n #n - off
        self.PROBABILITY = 45
        self.PRINTONRESET = False

        for i in range(len(napisyWiersze)):
            if(len(napisyWiersze[i]) == 1):
                for j in range(len(napisyWiersze[i][0])):
                    self.coloring[i][j] = napisyWiersze[i][0][j]
                    self.start_pos[i][j] = napisyWiersze[i][0][j]
                self.dobreWiersze.add(i)
                # print("wiersze: " )
                # print(napisyWiersze[i][0])
        for i in range(len(napisyKolumny)): 
            if(len(napisyKolumny[i]) == 1):
                for j in range(len(napisyKolumny[i][0])):
                    # print(napisyKolumny[i][0][j])
                    self.coloring[j][i] = napisyKolumny[i][0][j]
                    self.start_pos[j][i] = napisyKolumny[i][0][j]
                self.dobreKolumny.add(i)
        #         print("kolumny: ")
        #         print(napisyKolumny[i][0])
        # print(self.dobreKolumny)
        # print(self.dobreWiersze)
        # print(self.coloring)
        # exit(0)
        for i in range(len(napisyWiersze)):
            if i not in self.dobreWiersze:
                self.dozwoloneWiersze.append(i)
        for i in range(len(napisyKolumny)):
            if i not in self.dobreKolumny:
                self.dozwoloneKolumny.append(i)

    def correct_sequence(self, numbers: list, row: int, type=0):
        if(type == 0):
            if opt_dist_col(numbers, row) == 0:
                return True
        else:
            if opt_dist_row(numbers, row) == 0:
                return True
        return False
    
    def badRows(self):
        idx = -1
        score = 0
        rowne = []
        for i, row in enumerate(self.coloring):
            d = opt_dist_row(row, i)
            if d > score:
                if score > self.INSTANT_NAPRAWA_WIERSZ:
                    return idx
                score = d
                idx = i 
                rowne = [i]
            if d == score and score > 0:
                rowne.append(i)
        if len(rowne) > 0: #rozstrzygamy remis losowo
            return random.choice(rowne)
        return idx

    def pixel_score(self, columnNumber, pixel):
        col = np.copy(self.coloring[:, columnNumber])
        score1 = opt_dist_col(col, columnNumber)
        col[pixel] = (col[pixel] + 1) % 2
        score2 = opt_dist_col(col, columnNumber)
        return score1 - score2

    def check_columns(self):
        for i in range(self.m):
            col = np.copy(self.coloring[:, i])
            if not self.correct_sequence(col, i, 0):
                return False
        return True

    def randDecision(self):
        return random.randrange(0, 100) < self.PROBABILITY
    
    def wybierzKolumne(self, rowNumber):
        column_score = 0
        column_number = -1
        for c in range(self.m):
            score = self.pixel_score(c, rowNumber)
            if(score > self.INSTANT_NAPRAWA_KOLUMNA):
                return c
            if score > column_score:
                column_score = score
                column_number = c
        return column_number
    

    def solve(self): 
        tests = 0
        while tests < self.depth:
            tests += 1

            incorrectRow = self.badRows()
            if(incorrectRow == -1 and self.check_columns()):
                print(self.resets)
                return 
            if incorrectRow == -1:
                incorrectRow = random.choice(self.dozwoloneWiersze)

            column_number = self.wybierzKolumne(incorrectRow)
            
            if(column_number == -1 or self.randDecision()):
                try:
                    column_number = random.choice(self.dozwoloneKolumny)
                except:
                    pass
            
            self.coloring[incorrectRow][column_number] = (self.coloring[incorrectRow][column_number] + 1) % 2

        self.resets += 1
        if self.PRINTONRESET:
            self.print1()
        #add reset?
        self.coloring = np.copy(self.start_pos)
        self.solve()

    def print1(self):
        for i in self.coloring:
            for j in i:
                if j == 1:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def print_to_file(self):
        f = open("zad_output.txt", "w")
        for i in self.coloring:
            for j in i:
                if j == 1:
                    f.write("#")
                else:
                    f.write(".")
            f.write("\n")


def data_input():
    f = open("zad_input.txt")
    n, m = f.readline().split()
    n = int(n)
    m = int(m)
    rows = []
    for _ in range(n):
        a = list(map(int, f.readline().split()))
        rows.append(a)
    columns = []
    for _ in range(m):
        a = list(map(int, f.readline().split()))
        columns.append(a)
    return n, m, rows, columns


if "__main__" == __name__:
    n, m, rows, columns = data_input()
    for i in range(len(rows)):
        generuj2(m, rows[i])
        napisyWiersze.append(napisy)
        napisy = []
    for i in range(len(columns)):
        generuj2(n, columns[i])
        napisyKolumny.append(napisy)
        napisy = []
    #generuje poprawnie napisy
    nonogram = nonogram(n, m, rows, columns)
    # print(nonogram.dobreWiersze)
    nonogram.solve()
    nonogram.print_to_file()
    # print(len("0000000000000"))
    # print(opt_dist("11000", [1, 2]))
