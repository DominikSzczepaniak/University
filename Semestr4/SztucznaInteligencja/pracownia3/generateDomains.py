import subprocess

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

n,m,rows,cols = input_data()
napisyWiersze = []
napisyKolumny = []
for i in range(len(rows)):
    generuj2(m, rows[i])
    napisyWiersze.append(napisy)
    napisy = []
change_strings_to_lists(napisyWiersze)
for i in range(len(cols)):
    generuj2(n, cols[i])
    napisyKolumny.append(napisy)
    napisy = []
change_strings_to_lists(napisyKolumny)

#print all data back to zad_input:
with open("zad_input.txt", "w") as file:
    file.write(str(n) + " " + str(m) + "\n")
    for row in rows:
        file.write(" ".join([str(i) for i in row]) + "\n")
    for col in cols:
        file.write(" ".join([str(i) for i in col]) + "\n")
    for row in napisyWiersze:
        file.write("NewRow\n")
        for napis in row:
            file.write(" ".join([str(i) for i in napis]) + "\n")
    for col in napisyKolumny:
        file.write("NewRow\n")
        for napis in col:
            file.write(" ".join([str(i) for i in napis]) + "\n")
    file.write("NewRow\n")

subprocess.run(["./a.out"])
