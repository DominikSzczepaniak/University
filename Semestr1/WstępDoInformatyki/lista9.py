from wdi import Array
#zad1 skip
#zad2 
def zad2(n): #done
    b = Array(n+1)
    for i in range(n+1):
        b[i] = -1
    def isfree(x, y):
        for i in range(x):
            if b[i]-i==y-x or b[i]+i==y+x or b[i]==y:
                return 0 
        return 1
    def queens():
        b[0]=0
        k=1 
        wyniki = 0
        while k>=0:
            if(k == n):
                wyniki+=1
                k-=1
            b[k]+=1
            while b[k]<n and not isfree(k,b[k]):
                b[k]+=1
            if b[k]<n: 
                k+=1 
            else:
                b[k]=-1; k-=1 #brak wolnego pola, powrót do poprzedniej kolumny 
        return wyniki
    print(queens())
# zad2(9)
def zad3(): #done

    def isfree(x, y, b):
        for i in range(x):
            if b[i]-i==y-x or b[i]+i==y+x or b[i]==y:
                return 0 
        return 1
    def poprawne(a, n):
        for i in range(n):
            if(isfree(i, a[i], a) == False):
                return 0
        return 1
    def hetmany(n, k, a):
        if k==n: 
            return poprawne(a,n)
        for i in range(n):
            a[k]=i
            if (hetmany(n,k+1,a)): 
                return 1
        return 0
    print(hetmany(4, 0, [-1, -1, -1, -1]))
# zad3()
#a) nie rozumiem pytania - hetmany zwracaja 1 lub 0, nie rozwiazuja problemu hetmanow tylko mowia czy istnieje jakies ustawienie. co wpisac zeby rozwiazac? hetmany(8, 0, [-1, -1, -1, -1, -1, -1, -1,-1])
#b) done
#c) ta druga, bo nie zatrzymuje sie gdy znajdzie odpowiedz tylko sprawdza kolejne mozliwosci

#zad4: poki co skip

def zad5(n): #done
    def koniec(plansza):
        for i in range(n):
            for j in range(n):
                if(plansza[i][j] == 0):
                    return False
        return True
    def poprawna(plansza):
        uzyte = []
        suma = int((n * (n*n + 1))/2)
        for i in range(n):
            for j in range(n):
                if plansza[i][j] != 0:
                    if plansza[i][j] in uzyte:
                        return False
                    else:
                        uzyte.append(plansza[i][j])
                
        kolumna = []
        for i in range(n):
            kol = []
            for j in range(n):
                kol.append(plansza[j][i])
            kolumna.append(kol)
        przekatna1 = [plansza[i][i] for i in range(n)]
        przekatna2 = [plansza[i][n-i-1] for i in range(n)]

        for i in range(n):
            if 0 not in plansza[i] and sum(plansza[i]) != suma:
                return False
        
        for i in range(n):
            if 0 not in kolumna[i] and sum(kolumna[i]) !=suma:
                return False
        
        if 0 not in przekatna1:
            if sum(przekatna1) != suma:
                return False

        if 0 not in przekatna2:
            if sum(przekatna2) != suma:
                return False
        return True

    def puste_pole(plansza):
        for i in range(n):
            for j in range(n):
                if(plansza[i][j] == 0):
                    return i, j
    def nawrot(plansza):
        if(koniec(plansza) == True):
            return plansza 
        y, x = puste_pole(plansza)
        for liczba in range(1, n*n+1):
            plansza[y][x] = liczba 
            if(poprawna(plansza) == True):
                kolejny_krok = nawrot(plansza)
                if(koniec(kolejny_krok) == True):
                    return kolejny_krok
            plansza[y][x] = 0
        return plansza
    plansza_pusta = [[0 for i in range(n)] for j in range(n)]
    print(nawrot(plansza_pusta))
# zad5(3)
def zad6(n, a): #done
    plansza = [[0 for i in range(n)] for j in range(n)]
    plansza[0][0] = a[0][0]
    for i in range(1, n):
        plansza[0][i] = plansza[0][i-1] + a[0][i]
        plansza[i][0] = plansza[i-1][0] + a[i][0]
    for i in range(1, n):
        for j in range(1, n):
            plansza[i][j] = a[i][j]+min(plansza[i-1][j], plansza[i][j-1])
    # return plansza
    return plansza[n-1][n-1]
# print(zad6(3, [[10, 9, 31], [21, 7, 8], [13, 14, 10]]))
