from math import sqrt
def invert(f, a, b, y, n):
    start = a
    end = b
    while(start < end and n > 0):
        n -= 1
        mid = (start+end)/2
        if(f(mid) > y):
            end = mid
        else:
            start = mid
    return start
print(invert(lambda x: x*x, 0, 5, 5, 9))

wynik = sqrt(5)
for i in range(0,16):
    wartosc = invert(lambda x: x*x, 0, 5, 5, i)
    print(wartosc, wynik-wartosc)


