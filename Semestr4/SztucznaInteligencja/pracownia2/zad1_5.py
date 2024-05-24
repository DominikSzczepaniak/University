import numpy as np
from itertools import combinations


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


class Nonogram:
    def __init__(self):
        self.n, self.m, self.row_val, self.col_val = input_data()
        self.correct_rows = [False] * self.n
        self.correct_columns = [False] * self.m
        self.coloring = np.array([[False] * self.m] * self.n)

    def save_to_file(self):
        with open("zad_output.txt", "w") as file:
            for row in self.coloring:
                file.write("".join(['#' if i else '.' for i in row]) + "\n")

    def is_correct(self, domain_row, domain_col):
        for i, row in enumerate(self.coloring):
            if tuple(row) not in domain_row[i]:
                return False
        for col in range(self.m):
            if tuple(self.coloring[:, col]) not in domain_col[col]:
                return False

        return True

    @staticmethod
    def calculate(iter_space, iter_val):
        res = []
        for row in iter_space:
            act_res = []
            max_w = iter_val - row[-1]
            for combination in combinations(range(max_w + 1), len(row)):
                blocks_dont_overlap = True
                for cell in range(1, len(combination)):
                    if combination[cell - 1] + row[cell - 1] >= combination[cell]:
                        blocks_dont_overlap = False
                        break
                if blocks_dont_overlap:
                    new = [0] * iter_val
                    row_ptr = 0
                    for cell in combination:
                        for j in range(cell, cell + row[row_ptr]):
                            new[j] = 1
                        row_ptr += 1
                    act_res.append(new)
            res.append({tuple(i) for i in act_res})
        return res

    def get_possible_domains(self):
        return [self.calculate(self.row_val, self.m), self.calculate(self.col_val, self.n)]

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
    
    def solve_ac3(self):
        domain_row, domain_col = self.get_possible_domains()

        while not self.is_correct(domain_row, domain_col):
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


nonogram = Nonogram()
nonogram.solve_ac3()
nonogram.save_to_file()
