from wdi import *
from math import log2
#done
#test
def zad1():
    #a
    n = scanf("%d")
    odpa = -1 * n
    odpb = (-1)/float(n)
    #a O(1)
    if(n%2==0):
        odpa = n
    #b O(1)
    if(n%2==0):
        odpb = 1/float(n)
    #c 
    x = scanf("%d")
    odpc = 0
    potegi = Array(n+1)
    potegi[0] = 1
    for i in range(1, n+1):
        potegi[i] = potegi[i-1] * x
    for i in range(1, n+1):
        odpc += i * potegi[i]
    printf("a: %d, b: %f, c: %d", odpa, odpb, odpc)
#done
def zad2():
    def gcd(a, b):
        if(a==0):
            return b
        return gcd(b%a, a)
    a, b = scanf("%d %d")
    nwd = gcd(a, b)
    a /= nwd
    b /= nwd 
    printf("%d / %d", a, b)
#done
def zad3():
    def gcd(a, b):
        if(a==0):
            return b
        return gcd(b%a, a)
    n = scanf("%d")
    tab = Array(n)
    for i in range(n):
        tab[i] = scanf("%d")
    nwd = gcd(tab[0], tab[1])
    for i in range(2, n):
        nwd = gcd(nwd, tab[i])
    printf("%d", nwd)
#done
def zad4():
    n = scanf("%d")
    k = scanf("%d")
    liczby = Array(k)
    limit = Array(k)
    potegi = Array(k, log2(n)+10)
    for i in range(k):
        liczby[i]=scanf("%d")
        potegi[i][0] = 1
        for j in range(1, log2(n)+5):
            potegi[i][j] = potegi[i][j-1]*liczby[i]
            if(potegi[i][j] > n):
                limit[i] = j
                break
    maxP = 0
    ile = 0
    wyjscie = Array(k)
    for i in range(k):
        liczba = liczby[i]
        start = 0
        end = limit[i]
        while(start < end):
            mid = (start+end+1)//2
            if(n % potegi[i][mid] != 0):
                end = mid-1
            else:
                start = mid
        if(start > maxP):
            maxP = start
            wyjscie[0] = liczba 
            ile = 1
        elif(start == maxP):
            wyjscie[ile] = liczba 
            ile+=1
    print(maxP, end = " ")
    for i in range(ile):
        print(wyjscie[i], end = " ")
    #k * log(n) - liczenie poteg, w najgorszej opcji moge dostac same dwojki, wtedy musze robic potegi log2(n) razy, dla kazdego innego przypadku bedzie lepiej 
    #k * log(log(n)) - szukanie binarnie ile razy sie miesci dana potega - z poprzedniego punktu wiemy ze najwiecej moze byc log(n) dwojek, wiec wykona log(log(n)) w binarnym
    #to drugie amortyzuje sie do k*log(n), wiec zlozonosc jest k*log(n)

#done
def zad5():
    def isPalindrom(s):
        for i in range(int(len(s))//2):
            if(s[i] != s[int(len(s))-1-i]):
                return False
        return True
    def zamien_na_system(podstawa_systemu, liczba): #O(log podstawa_systemu (liczba)) + O(10) = O(log podstawa_systemu (liczba))
        ciag = Array(int(log2(liczba))+10)
        miejsce = 0
        while(liczba > 0):
            reszta = int(liczba%podstawa_systemu)
            ciag[miejsce] = reszta
            liczba //= podstawa_systemu
            miejsce+=1
        # print(ciag)
        s = ""
        for i in range(miejsce, -1, -1):
            s = s + str(ciag[i])
        while(s[0] == "0"):
            s = s[1::]
        return s
        # start = 0
        # while(s[start] != "1"):
        #     start+=1 
        # napis = ""
        # for i in range(start, len(s)):
        #     napis += s[i]
        # return napis
    n = scanf("%d")
    s = zamien_na_system(2, n)
    print(s)
    if(isPalindrom(s)):
        printf("Tak")
    else:
        printf("Nie")
#done
def zad6():
    #Palindromem k-arnym będziemy nazywać liczbę która w zapisie o podstawie k ma tę własność, że „czytana od końca” jest równa liczbie oryginalnej; np. 303, 321123, 8778
    #Specyfikacja: 
    #Wejscie: k, liczba podana w k-arnym systemie liczbiowym
    #wyjscie: Tak / nie jesli liczba jest palindromem k-arnym
    #Zlozonosc: O(N)
    def isPalindrom(s):
        for i in range(int(len(s))//2):
            if(s[i] != s[int(len(s))-1-i]):
                return False
        return True
    k = scanf("%d")
    n = scanf("%d")
    def zamien_na_system(podstawa_systemu, liczba): #O(log podstawa_systemu (liczba))
        ciag = Array(int(log2(liczba))+10)
        miejsce = 0
        while(liczba > 0):
            reszta = int(liczba%podstawa_systemu)
            ciag[miejsce] = reszta
            liczba //= podstawa_systemu
            miejsce+=1
        # print(ciag)
        s = ""
        for i in range(miejsce, -1, -1):
            s = s + str(ciag[i])
        while(s[0] == "0"):
            s = s[1::]
        return s
        # start = 0
        # while(s[start] != "1"):
        #     start+=1 
        # napis = ""
        # for i in range(start, len(s)):
        #     napis += s[i]
        # return napis
    s = zamien_na_system(k, n)
    if(isPalindrom(s)):
        printf("Tak")
    else:
        printf("Nie")
#done
def zad7():
    n = scanf("%d")
    cyfry = Array(10)
    while(n>0):
        cyfry[n%10] += 1
        n //= 10
    wynik = 0
    for i in range(10):
        if(cyfry[i] > 0):
            wynik += 1
    printf("%d", wynik)
#done
def zad8():
    n, m = scanf("%d %d")
    cyfry1 = Array(10)
    cyfry2 = Array(10)
    while(n>0):
        cyfry1[n%10] += 1
        n //= 10
    while(m>0):
        cyfry2[m%10] += 1
        m //= 10
    for i in range(10):
        if(cyfry1[i] != cyfry2[i]):
            printf("Nie")
            return
    printf("Tak")



    
        