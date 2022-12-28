from wdi import *
from math import log2

#done 
def zad2():
    n = scanf("%d")
    silnie = Array(n+1)
    silnie[0] = 1
    end = n
    for i in range(1, n+1):
        silnie[i] = silnie[i-1] * i
        if(silnie[i] >= n):
            end = i 
            break 
    start = 0
    while(start < end):
        mid = (start+end+1)//2
        if(silnie[mid] > n):
            end = mid-1
        else:
            start = mid
    reprezentacja = Array(start+1)
    for i in range(start, -1, -1):
        start_ilosc = 0
        end_ilosc = n
        while(start_ilosc < end_ilosc):
            mid = (start_ilosc+end_ilosc+1)//2
            if(silnie[i] * mid <= n):
                start_ilosc = mid 
            else:
                end_ilosc = mid-1
        reprezentacja[i] += start_ilosc
        n -= silnie[i] * start_ilosc
    for i in range(start, 0, -1):
        print(f"{reprezentacja[i]}", end = " ")
    print()
    #rozpiszmy liczbe jako a * 1! + b*2! + c*3! + ... 
    #pokazmy, ze jezeli mamy jakies liczbe przy silni to jesli jest wieksza niz jej silnia, to mozemy ja zapisac jako (n+1)!
    #czyli np jak mamy 3*2! to to jest rowne 3!. Więc bierzmy po prostu jak najwięcej silni mozemy i wtedy na pewno nie przekroczymy poprzedniej liczby, bo wzielismy obecnie najwieksza liczbe silni.
zad2()
#done
def zad4():
    n = scanf("%d")
    liczby = Array(3)
    liczby[0] = liczby[1] = liczby[2] = 1
    wskaznik = 0
    i = 3
    while(i<=n):
        liczby[wskaznik] = liczby[0] + liczby[1] + liczby[2]
        wskaznik = (wskaznik+1)%3
        i+=1
    print(liczby[(3+wskaznik-1)%3])
#done 
def zad5():
    def rekurencyjna(n, m):
        if(n>=0 and m == 0):
            return n
        elif(n == 0 and m >= 0):
            return m
        else:
            return rekurencyjna(n-1, m) + 2*rekurencyjna(n, m-1)
    #DO NARYSOWANIA DRZEWO WYWOLAN
    def nierekurencyjna(n, m):
        T = Array(n+1, m+1)
        for i in range(n+1):
            T[i][0] = i 
        for i in range(m+1):
            T[0][i] = i
        for i in range(1, n+1):
            for j in range(1, m+1):
                T[i][j] = T[i-1][j] + 2 * T[i][j-1]
        return T[n][m]
#done
def zad6():
    def fibonacci(k, r):
        F = Array(k+1)
        F[1] = 1
        F[2] = 1
        for i in range(3, k+1):
            F[i] = (F[i-1]%r+F[i-2]%r)%r
        return F[k]
    #zapiszmy a jako k*c + d, gdzie k jest dowolna liczba naturalna
    #zapiszmy b jako l*c + e, gdzie l jest dowolna liczba naturalna
    #d i e < c
    #a+b = kc + d + lc + e = c(k+l) + d + e
    #c(k+l) = 0 mod c
    #wiec a + b = (e+d) mod c
    #(a mod c) + (b mod c) mod c = (kc + d mod c) + (lc + e mod c) mod c = (d moc c) + (e mod c) mod c = (d + e) moc c = (a + b) mod c
#done
def zad7():
    n = scanf("%d")
    m = scanf("%d")
    def szybkaPot(a, b):
        rez = 1 
        while b>0:
            if b%2:
                rez = rez * a
            b = b // 2
            a=a* a 
        return rez
    start = 0
    end = log2(m)+10
    while(start < end):
        mid = (start+end)//2
        if(szybkaPot(n, mid) >= m):
            end = mid 
        else:
            start = mid+1
    print(start)
    #moge zrobic log*log(k) log(k) jest tak male ze to i tak nie ma znaczenia prawie w ogole wiec log(k) jest prawie jak log(log(k))

