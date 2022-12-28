from duze_cyfry import daj_cyfre

def liczba(n):
    n = int(input())
    A = []
    ile = 0
    for j in str(n):
        A.append(daj_cyfre(int(j)))
        ile+=1
    print(A)
    wynik = [[]]
    for j in range(0, 5):
        for i in range(ile):
            wynik[j].append(A[i][j])
            wynik[j].append(" ")
        wynik.append([])
    return wynik


