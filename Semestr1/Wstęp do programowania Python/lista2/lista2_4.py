from duze_cyfry import daj_cyfre

n = int(input())
A = []
ile = 0
for j in str(n):
    A.append(daj_cyfre(int(j)))
    ile+=1
print(A)
for j in range(0, 5):
    for i in range(ile):
        print(A[i][j], end = "")
        print(end = " ")
    print()