import numpy as np
from itertools import combinations
from copy import deepcopy, copy



def input_data():
    with open("zad_input.txt", "r") as file:
        n, m = map(int, file.readline().split())

        row_val = []
        col_val = []
        for _ in range(n):
            row_val.append(list(map(int, file.readline().strip('\n').split())))
        for _ in range(m):
            col_val.append(list(map(int, file.readline().strip('\n').split())))
        return n, m, row_val, col_val

def change_strings_to_lists(domain):
    for d in domain:
        for i in range(len(d)):
            d[i] = [int(j) for j in d[i]]
#najpierw za pomoca ac_3 obcinamy domeny tak zeby bylo ich jak najmniej

#pozniej backtrackiem wybieramy domene i usuwamy wszystkie domeny ktore nie pasuja do tej i idziemy dalej. jesli nie znajdziemy wynik to wracamy (typowy backtrack, ale po domenach)

#założenia:
#domeny są listami list, nie listami stringów

#zamiast uzywać .end() zaznaczajmy te kolumny i wiersze które są poprawne.

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
        answer = ""
        i = 0
        for d in self.rowDomains:
            i += 1
            answer += ("row: %d" % i) + "\n"
            answer += str(d) + "\n"
        answer += "\n"
        i = 0
        for d in self.colDomains:
            i += 1
            answer += ("col: %d" % i) + "\n"
            answer += str(d) + "\n"
        return answer

class Nonogram:
    def __init__(self):
        self.n, self.m, self.rows, self.cols = input_data()
        self.coloring = np.array([[False] * self.m] * self.n)

        global napisy
        self.napisyWiersze = []
        self.napisyKolumny = []
        for i in range(len(self.rows)):
            generuj2(self.m, self.rows[i])
            self.napisyWiersze.append(napisy)
            napisy = []
        change_strings_to_lists(self.napisyWiersze)
        for i in range(len(self.cols)):
            generuj2(self.n, self.cols[i])
            self.napisyKolumny.append(napisy)
            napisy = []
        change_strings_to_lists(self.napisyKolumny)
        self.csp = CSP(self.napisyWiersze, self.napisyKolumny)
        # del self.napisyWiersze 
        # del self.napisyKolumny

    def save_to_file(self):
        with open("zad_output.txt", "w") as file:
            for row in self.coloring:
                file.write("".join(['#' if i else '.' for i in row]) + "\n")

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

    

    @staticmethod
    def domain_remover(csp: CSP, i, j, value):
        #TODO: optimise:
            #1. remove those that will exceed maximum number of possible 1s
            #2. remove those that will not fit in the row - for example we need 3 and 1 on 5 length but we put 1 at the middle, then 3 wont fit (i think it has smth to do with opt_dist eg. if its higher than length - colored already than its bad?)
        newRowDomains = []
        for row in csp.rowDomains[i]:
            if str(row[j]) == value:
                #csp.rowDomains[i].remove(row)
                newRowDomains.append(row)
        csp.rowDomains[i] = newRowDomains
            
        newColumnDomains = []
        for col in csp.colDomains[j]:
            if str(col[i]) == value:
                # csp.colDomains[j].remove(col)
                newColumnDomains.append(col)
        csp.colDomains[j] = newColumnDomains

        return csp
    
    
    def domain_sum_optimise(self, csp: CSP):
        #if sum of ones in some column is bigger than value in cols then remove 
        goodColumns = []
        for i, col in enumerate(csp.colDomains):
            suma = sum(row.count(1) for row in col)
            if suma != self.cols[i]:
                goodColumns.append(col)
        #if sum of ones in some row is bigger than value in rows then remove
        goodRows = []
        for i, row in enumerate(csp.rowDomains):
            suma = sum(col.count(1) for col in row)
            if suma != self.rows[i]:
                goodRows.append(row)
        csp.colDomains = goodColumns
        csp.rowDomains = goodRows
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

    def is_correct(self, domain_row, domain_col):
        for i, row in enumerate(self.coloring):
            if tuple(row) not in domain_row[i]:
                return False
        for col in range(self.m):
            if tuple(self.coloring[:, col]) not in domain_col[col]:
                return False

        return True
    
    @staticmethod
    def domain_intersection(domain):
        i1 = list(domain)[0]
        i2 = list(domain)[0]

        for poss in domain:
            i1 = [1 if poss[i] == 1 and i1[i] == poss[i] else 0 for i in range(len(poss))]
            i2 = [0 if poss[i] == 0 and i2[i] == poss[i] else 1 for i in range(len(poss))]
        return i1, i2

    @staticmethod
    def remove_not_fitting(cells, domain, color, is_row):
        if is_row:
            for r, c in cells:
                to_clear = []
                for poss in domain[c]:
                    if poss[r] != color:
                        to_clear.append(poss)
                for rm in to_clear:
                    domain[c] -= {rm}
        else:
            for r, c in cells:
                to_clear = []
                for poss in domain[r]:
                    if poss[c] != color:
                        to_clear.append(poss)
                for rm in to_clear:
                    domain[r] -= {rm}
        return domain
    

    def solve_ac3(self, csp: CSP):
        domain_row = []
        domain_col = []
        for i in range(self.n):
            dodaj = set()
            for j in range(len(csp.rowDomains[i])):
                dodaj.add(tuple(csp.rowDomains[i][j]))
            domain_row.append(dodaj)
        for i in range(self.m):
            dodaj = set()
            for j in range(len(csp.colDomains[i])):
                dodaj.add(tuple(csp.colDomains[i][j]))
            domain_col.append(dodaj)
        # domain_row, domain_col = set(self.napisyWiersze.copy()), set(self.napisyKolumny.copy())
        last_domain_row, last_domain_col = copy(domain_row), copy(domain_col)
        ile = 0
        while True:
            # --- row ---
            chosen_cells = set()
            unchosen_cells = set()

            r = 0
            for row in domain_row:
                c = 0

                intersection = self.domain_intersection(row)
                for cell in range(len(intersection[0])):
                    if intersection[0][cell] == 1:
                        self.coloring[r][c] = True
                        chosen_cells.add((r, c))

                    if intersection[1][cell] == 0:
                        self.coloring[r][c] = False
                        unchosen_cells.add((r, c))
                    c += 1

                r += 1
            domain_col = self.remove_not_fitting(chosen_cells, domain_col, 1, True)
            domain_col = self.remove_not_fitting(unchosen_cells, domain_col, 0, True)

            # --- col ---
            chosen_cells = set()
            unchosen_cells = set()

            c = 0
            for col in domain_col:
                r = 0

                intersection = self.domain_intersection(col)
                for cell in range(len(intersection[0])):
                    if intersection[0][cell] == 1:
                        self.coloring[r][c] = True
                        chosen_cells.add((r, c))

                    if intersection[1][cell] == 0:
                        self.coloring[r][c] = False
                        unchosen_cells.add((r, c))
                    r += 1

                c += 1

            domain_row = self.remove_not_fitting(chosen_cells, domain_row, 1, False)
            domain_row = self.remove_not_fitting(unchosen_cells, domain_row, 0, False)


            if(domain_row == last_domain_row and domain_col == last_domain_col):
                ile += 1
                if ile == 50:
                    break

            last_domain_col = copy(domain_col)
            last_domain_row = copy(domain_row)

        return last_domain_row, last_domain_col





class Solve:
    def __init__(self, nonogram: Nonogram):
        self.nonogram = nonogram
        self.ile = 0
        ac3_answer = self.nonogram.solve_ac3(nonogram.csp)
        print("koniec ac3")
        # self.nonogram.save_to_file()
        # return
        csp_new = deepcopy(CSP(ac3_answer[0], ac3_answer[1]))
        # opcje_rows = 1
        # for i in range(len(csp_new.rowDomains)):
        #     opcje_rows *= len(csp_new.rowDomains[i])
        # opcje_cols = 1
        # for i in range(len(csp_new.colDomains)):
        #     opcje_cols *= len(csp_new.colDomains[i])
        # print("here", opcje_rows, opcje_cols)
        print(csp_new.rowDomains[0])
        return
        self.solve(csp_new, np.array([[False] * self.nonogram.m] * self.nonogram.n))
        nonogram.save_to_file()

    def solve(self, csp: CSP, coloring, current_row=0):

        #dodaj ac3 -> backtrack
        if current_row==self.nonogram.n:
            if self.nonogram.end(coloring):
                self.nonogram.coloring = coloring
                self.nonogram.save_to_file()
                return True
            else:
                return False
        for row_config in csp.rowDomains[current_row]:
            temp_coloring = coloring.copy()
            temp_coloring[current_row] = row_config

            new_csp = deepcopy(csp)
            valid = True
            for j, val in enumerate(temp_coloring[current_row]):
                if val:
                    new_csp = Nonogram.domain_remover(new_csp, current_row, j, "1")
                else:
                    new_csp = Nonogram.domain_remover(new_csp, current_row, j, "0")
                new_csp = nonogram.domain_sum_optimise(new_csp)
                if Nonogram.check_if_empty_domain(new_csp):
                    valid = False
                    break

            if valid and self.solve(new_csp, temp_coloring, current_row+1):
                return True

            coloring[current_row] = np.array([False] * self.nonogram.m)

        # print("unpossible")






nonogram = Nonogram()
# print(nonogram.csp)
solver = Solve(nonogram)
