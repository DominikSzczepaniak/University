import random
from zad4 import opt_dist
import numpy as np


class nonogram():
    def __init__(self, n, m, rows, columns):
        self.n = n
        self.m = m
        self.rows = rows
        self.columns = columns
        self.coloring = np.random.randint(2, size=(n, m))
        self.depth = 7000

    def correct_sequence(self, number, row):
        if opt_dist(row, number) == 0:
            return True
        return False

    def incorrect_rows(self):
        result = []
        for i in range(len(self.coloring)):
            if not self.correct_sequence(self.rows[i], self.coloring[i]):
                result.append(i)
        return result

    def pixel_score(self, columnNumber, pixel):
        col = np.copy(self.coloring[:, columnNumber])
        score1 = opt_dist(col, self.columns[columnNumber])
        col[pixel] = (col[pixel] + 1) % 2
        score2 = opt_dist(col, self.columns[columnNumber])
        return score1 - score2

    def check_columns(self):
        for i in range(self.m):
            col = np.copy(self.coloring[:, i])
            if not self.correct_sequence(self.columns[i], col):
                return False
        return True


    def randDecision(self):
        return random.randrange(0, 5) < 1


    def solve(self):
        tests = 0
        while tests < self.depth:
            incorrectRows = self.incorrect_rows()
            if not incorrectRows:
                if self.check_columns():
                    return
                else:
                    random_number = random.randrange(0, self.n)
            else:
                random_number = random.choice(incorrectRows)

            if self.randDecision():
                random_number = random.randrange(0, self.n)

            columns_scores = [c for c in range(self.m) if self.pixel_score(c, random_number) > 0 or self.randDecision()]

            if not columns_scores:
                column_number = random.randrange(0, self.m - 1)
            else:
                column_number = random.choice(columns_scores)

            self.coloring[random_number][column_number] = (self.coloring[random_number][column_number] + 1) % 2
        self.solve()

    def print1(self):
        print("   ", end="")
        for i in self.columns:
            print(i, end=" ")
        print()
        for i in range(len(rows)):
            print(self.rows[i], end=" ")
            print(self.coloring[i])

    def print_to_file(self):
        f = open("zad5_output.txt", "w")
        for i in self.coloring:
            for j in i:
                if j == 1:
                    f.write("#")
                else:
                    f.write(".")
            f.write("\n")


def data_input():
    f = open("zad5_input.txt")
    n, m = f.readline().split()
    n = int(n)
    m = int(m)
    rows = []
    for i in range(n):
        a = int(f.readline())
        rows.append(a)
    columns = []
    for i in range(m):
        a = int(f.readline())
        columns.append(a)
    return n, m, rows, columns


if "__main__" == __name__:
    n, m, rows, columns = data_input()
    nonogram = nonogram(n, m, rows, columns)
    nonogram.solve()
    nonogram.print_to_file()
