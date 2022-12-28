#zad1 done
#T(n) = T(n-1) + n = T(n-2) + n-1 + n = 1 + 2 + 3 + 4 + ... + n-1 + n = ((1+n)*n)/2
def zad1():
    def T(n):
        if(n == 1):
            return 1
        return T(n-1) + n
    T(16)
#zlozonosc liniowa - nie wiem, szukanie minmax iteracyjnie?

#zad 2
#T(1) = 0
#T(n) = T(n/2) + 1 dla parzystego n
#T(n) = T((n+1)/2)+1 dla nieparzystego n
#T(16) = T(8) + 1 = T(4) + 2 = T(2) + 3 = T(1) + 4 = 0 + 4 = 4
# n = 2^k dla k naturalnego wiec 2|n
#T(n) = T(n/2) + 1 = T(n/4) + 2 = T(n/8) + 3 = T(n/2^i) + i = T(n/2^k) + k = 0 + logn = logn = O(logn)

#zad 3 
#T(1) = 1
#T(n) = 2*T(n/2) + 1 dla parzystego n>1
#T(n) = T((n-1)/2) + T((n+1)/2) + 1 dla nieparzystego n
#T(n) = 2T(n/2) + 1 = 2*(2*T(n/4) + 1) + 1 = 4T(n/4) + 3 = 4(2(T(n/8) + 1)) + 3 = 2^i*T(n/2^i) + 2^i - 1 = 2^k * T(n/2^k) + 2^k - 1 = n * T(n/n) + n - 1 = n+n-1 = 2n - 1
#T(16) = 31

#zad5 done 
def zad5():
    def minimum(tablica, start, end):
        if(end == start):
            return tablica[end]
        m1 = minimum(tablica, start, start+(end-start)//2)
        m2 = minimum(tablica, start+(end-start)//2+1, end)
        return min(m1, m2)
    tablica = [1234,1234,12,43,1234,21,34,2143,321,4,21,43]
    print(minimum(tablica, 0 , len(tablica)-1))
#n - dlugosc tablicy
#w kazdej rekurencji dostajemy podzial obecnej tablicy na dwie, wiec bedziemy dostawac podzialy na dwie tak dlugo az dlugosc kazdej z tablicy bedzie jeden i wtedy bedziemy wracac
#T(1) = 0
#T(2) = 1
#T(n) = 2*T(n/2) + 1

# n = 2^k
#T(n) = 2*T(n/2) + 1 = 2*( 2* T(n/4) + 1)) + 1 = 2*2*T(n/4) + 2 + 1 = 2*2*(2 * T(n/8) + 1) + 2 = 1 + 2 + 4 + 8*T(n/8) = ... =  2^k - 1 + 2^k * T(n/2^k) = n - 1 + n * T(1) = n - 1
#zad6 done
#w a bedziemy miec najmniejsza wartosc i cala reszta bedzie wieksza wiec bedziemy miec najgorszy przypadek, ze w kazdym kroku sprawdzamy tablice o 1 mniejsza niz poprzednia, wiec zlozonosc O(n^2)
#w b bedziemy miec najwieksza wartosc i cala reszta bedzie szla na lewo, wiec tak samo jak w a, za kazdym razem bedziemy sprawdzac tablice o 1 mniejsza niz poprzednia, wiec O(n^2)
#w c zalezy od implementacji, jesli dzielimy na dwie tablice < i >= to za kazdym razem bedzie o tablica o 1 mniejsza wiec O(n^2)
#jesli robimy 3 tablice < = > to O(n), bo wszystko wejdzie od razu do = i mamy koniec (najczesciej uzywany format i to jest w linuxie na pewno jako podstaw
# jesli >= i <= to nie wykona zadnych zamian, wiec bedzie O(nlogn)
#zad7
#10 : 
#a) 
# log2(10) = 4
# log2(100) = 7
# log2(1000) = 10
#b)
# najmniejsza | najwieksza
# 4           | 10
# 7           | 100
# 10          | 1000
#zawsze na dwa|zawsze o 1 mniejsza
# log2(n)     | n
#zad8
#Specyfikacja: 
#wejscie: wysokosc wiezy
#wyjscie: lista instrukcji jak ulozyc wieze
def zad8():
    def hanoi(n, skad, dokad, przez_co):
        if n == 0:
            return
        hanoi(n-1, skad, przez_co, dokad)
        print("Dysk", n, "z", skad, "do", dokad)
        hanoi(n-1, przez_co, dokad, skad)
 
    hanoi(2, "A", "C", "B")
zad8()
