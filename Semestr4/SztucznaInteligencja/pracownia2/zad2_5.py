import numpy as np
from itertools import combinations
from copy import deepcopy



def input_data():
    with open("zad_input.txt", "r") as file:
        n, m = map(int, file.readline().split())

        row_val = []
        col_val = []
        for i in range(n):
            row_val.append(list(map(int, file.readline().strip('\n').split())))
        for i in range(m):
            col_val.append(list(map(int, file.readline().strip('\n').split())))
        return n, m, row_val, col_val

#jak zrobic
# mozemy wygenerowac wszystkie opcje i robic backtracking z forward checking?
#
# mozemy wygenerowac wszystkie opcje wierszy i kolumny
# wybierac losowe wiersze i kolumny
# jak zakolorujemy jakis pixel (i, j)
# to mozemy usunac wszystkie rzeczy z domeny kolumny j takie, ze pixel (i, j) nie jest zakolorowany
# i usunac wszystkie rzeczy z domeny wiersza i takie, ze pixel (i, j) nie jest zakolorowany
# jesli jakas domena dla ktoregos wiersza/kolumny jest pusta to mamy zle rozwiazanie i backtracking robimy
#

napisy = []
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

class CSP:
    rowDomains: list
    colDomains: list
    def __init__(self, rows, cols):
        self.rowDomains = rows
        self.colDomains = cols

    def __str__(self):
        return str(self.rowDomains) + "\n" + str(self.colDomains)

class Nonogram:
    def __init__(self):
        self.n, self.m, self.rows, self.cols = input_data()
        self.correct_rows = [False] * self.n
        self.correct_columns = [False] * self.m
        self.coloring = np.array([[False] * self.m] * self.n)
        self.not_done_cols = [i for i in range(self.m)]
        self.not_done_rows = [i for i in range(self.n)]
        global napisy
        self.napisyWiersze = []
        self.napisyKolumny = []
        for i in range(len(self.rows)):
            generuj2(self.m, self.rows[i])
            self.napisyWiersze.append(napisy)
            napisy = []
        for i in range(len(self.cols)):
            generuj2(self.n, self.cols[i])
            self.napisyKolumny.append(napisy)
            napisy = []
        self.csp = CSP(self.napisyWiersze, self.napisyKolumny)

    def opt_dist_col(self, napis, nrKolumny):
        min_wynik = len(napis)+5
        for i in self.napisyKolumny[nrKolumny]:
            wynik = 0
            for j in range(len(napis)):
                if(str(i[j]) != str(int(napis[j]))):
                    wynik += 1
            min_wynik = min(min_wynik, wynik)
        return min_wynik

    def opt_dist_row(self, napis, nrWiersza):
        min_wynik = len(napis)+5
        for i in self.napisyWiersze[nrWiersza]:
            wynik = 0
            for j in range(len(napis)):
                if(str(i[j]) != str(int(napis[j]))):
                    wynik += 1
            min_wynik = min(min_wynik, wynik)
        return min_wynik

    def end(self, coloring):
        for i in range(len(coloring)):
            if(self.opt_dist_row(coloring[i], i) != 0):
                return False
        for j in range(len(coloring[0])):
            if(self.opt_dist_col(coloring[:, j], j) != 0):
                return False
        return True

    def save_to_file(self):
        with open("zad_output.txt", "w") as file:
            for row in self.coloring:
                file.write("".join(['#' if i else '.' for i in row]) + "\n")

    @staticmethod
    def domain_remover(csp: CSP, i, j):
        #TODO: optimise:
            #1. remove those that will exceed maximum number of possible 1s
            #2. remove those that will not fit in the row - for example we need 3 and 1 on 5 length but we put 1 at the middle, then 3 wont fit
        for row in csp.rowDomains[i]:
            if str(row[j]) != "1":
                csp.rowDomains[i].remove(row)
        for col in csp.colDomains[j]:
            if str(col[i]) != "1":
                csp.colDomains[j].remove(col)
        return csp

    @staticmethod
    def check_if_empty_domain(csp: CSP):
        for row in csp.rowDomains:
            if len(row) == 0:
                return True
        for col in csp.colDomains:
            if len(col) == 0:
                return True
        return False

class Solve:
    def __init__(self, nonogram: Nonogram):
        self.nonogram = nonogram
        self.ile = 0
        self.solve(deepcopy(nonogram.csp), deepcopy(nonogram.coloring))

    @staticmethod
    def convert(arr):
        answer = []
        for i in arr:
            if i == "0":
                answer.append(False)
            else:
                answer.append(True)
        return answer

    def solve(self, csp: CSP, coloring, current_row=0):
        if current_row==self.nonogram.n:
            if self.nonogram.end(coloring):
                self.nonogram.coloring = coloring
                self.nonogram.save_to_file()
                return True
            else:
                return False
        for row_config in csp.rowDomains[current_row]:
            temp_coloring = coloring.copy()
            temp_coloring[current_row] = Solve.convert(row_config)

            new_csp = deepcopy(csp)
            valid = True
            for j, val in enumerate(temp_coloring[current_row]):
                if val:
                    new_csp = Nonogram.domain_remover(new_csp, current_row, j)
                    if Nonogram.check_if_empty_domain(new_csp):
                        valid = False
                        break

            if valid and self.solve(new_csp, temp_coloring, current_row+1):
                return True

            coloring[current_row] = np.array([False] * self.nonogram.m)

            # while i in nonogram.not_done_rows:
            #     if(nonogram.end(coloring)):
            #         nonogram.coloring = coloring
            #         nonogram.save_to_file()
            #         return
            #     coloring[i] = Solve.convert(csp.rowDomains[i][0])
            #     csp.rowDomains[i].remove(csp.rowDomains[i][0])
            #     new_csp = deepcopy(nonogram.csp)
            #     for pixel in range(len(coloring[i])):
            #         if str(coloring[i][pixel]) == "1":
            #             new_csp = Nonogram.domain_remover(new_csp, i, pixel)
            #     columns = True
            #     for j in range(self.nonogram.m):
            #         if sum(nonogram.cols[j]) < sum(coloring[:,j]):
            #             coloring[i] = np.array([False] * self.nonogram.m)
            #             columns = False
            #             break
            #     if not columns or Nonogram.check_if_empty_domain(new_csp) or sum(coloring[i]) > sum(nonogram.rows[i]):
            #         coloring[i] = np.array([False] * self.nonogram.m)
            #     else:
            #         nonogram.not_done_rows.remove(i)
            #         self.solve(new_csp, coloring)
            #         nonogram.not_done_rows.append(i)








nonogram = Nonogram()
solver = Solve(nonogram)
