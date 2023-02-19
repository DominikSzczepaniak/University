from math import gcd, factorial
from decimal import *
class R:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def __add__(self, other):
        licz = self.licznik*other.mianownik + other.licznik*self.mianownik
        mian = self.mianownik*other.mianownik
        nwd = gcd(licz, mian)
        licz = int(licz/nwd) 
        mian = int(mian/nwd)
        return R(licz, mian)
    def __sub__(self, other):
        return self+R(-other.licznik, other.mianownik) 
        licz = self.licznik*other.mianownik - other.licznik*self.mianownik
        mian = self.mianownik*other.mianownik
        nwd = gcd(licz, mian)
        licz = int(licz/nwd) 
        mian = int(mian/nwd)
        return R(licz, mian)
    def __mul__(self, other):
        licz = self.licznik*other.licznik
        mian = self.mianownik*other.mianownik
        nwd = gcd(licz, mian)
        licz = int(licz/nwd) 
        mian = int(mian/nwd)
        return R(licz, mian)
    def __truediv__(self, other):
        licz = self.licznik*other.mianownik
        mian = self.mianownik*other.licznik
        nwd = gcd(licz, mian)
        licz = int(licz/nwd) 
        mian = int(mian/nwd)
        return R(licz, mian)
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.licznik*other.mianownik == other.licznik*self.mianownik
    def __iadd__(self, other): 
        if(type(other) != R):
            other = R(other, 1)
        self.licznik = self.licznik*other.mianownik + other.licznik*self.mianownik
        self.mianownik = self.mianownik*other.mianownik 
        nwd = gcd(self.licznik, self.mianownik) 
        self.licznik = int(self.licznik/nwd)
        self.mianownik = int(self.mianownik/nwd)       
        return self
    def __isub__(self, other):
        if(type(other) != R): 
            other = R(other, 1)
        self.licznik = self.licznik*other.mianownik - other.licznik*self.mianownik
        self.mianownik = self.mianownik*other.mianownik
        nwd = gcd(self.licznik, self.mianownik)
        self.licznik = int(self.licznik/nwd) 
        self.mianownik = int(self.mianownik/nwd) 
        return self
    def __imul__(self, other):
        if(type(other) != R):
            other = R(other, 1)
        self.licznik = self.licznik*other.licznik
        self.mianownik = self.mianownik*other.mianownik
        nwd = gcd(self.licznik, self.mianownik)
        self.licznik = int(self.licznik/nwd)  
        return self
    def __itruediv__(self, other):
        if(type(other) != R):
            other = R(other, 1)
        self.licznik = self.licznik*other.mianownik
        self.mianownik = self.mianownik*other.licznik 
        nwd = gcd(self.licznik, self.mianownik)
        self.mianownik = int(self.mianownik/nwd) 
        return self
    def __radd__(self, other):
        other = R(other, 1)
        return self + other 
    def __rmul__(self, other):
        other = R(other, 1)
        return self*other
    def __rsub__(self, other):
        other = R(other, 1)
        return other - self
    def __rtruediv__(self, other):
        other = R(other, 1)
        return other/self
a = R(2, 5)
b = R(3, 5)
c = R(4, 5)
print([a, b, c])
print(a+b)
print(1+a)
print(a*b)
print(a/b)
print(a-b)
a += R(2,5)
print(a)
a += 1

#zad 8
#suma n od 0 do nieskonczonosci: 1/n!
#1/n! szybko maleje wiec do 30?
def isPrime(n):
    if(n == 1 or n == 0):
        return False 
    i = 2
    while(i * i <= n):
        if(n%i == 0):
            return False 
        i += 1 
    return True 
n = 50
wartosce = Decimal(0)
# wartosce = 0
setcontext(Context(prec=300))
for i in range(n+1):
    wartosce += Decimal(Decimal(1)/Decimal(factorial(i)))
    # wartosce += 1/factorial(i)
napis = str(wartosce)
print(f"{wartosce:.120f}")
for i in range(2, len(napis)-5):
    czesc_napisu = napis[i:i+5]
    if(czesc_napisu[0] == "0"):
        continue 
    liczba = int(czesc_napisu)
    if(isPrime(liczba) == True):
        print(liczba)
        break
