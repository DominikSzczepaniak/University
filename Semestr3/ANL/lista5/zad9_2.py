from math import log
def f(x):
    return x**3 + 7*x**2 - 5*x - 75
def fPrim(x):
    return 3*x**2 + 14*x - 5
def fDoublePrim(x):
    return 6*x + 14

def olverMethod(x):
    return x - f(x)/fPrim(x) - 1/2 * (fDoublePrim(x)/fPrim(x)) * (f(x)/fPrim(x))**2

def znajdz_p(r0,r1,r2,r3):
    start = 1
    end = 25
    licznik = 0
    while(start < end):
        licznik+=1
        if(licznik > 50):
            break
        mid = (start+end)/2
        C1 = r3/r2**mid
        C2 = r2/r1**mid
        print(mid, C1, C2)
        if(abs(C1-C2) < 4e-5):
            start = mid 
            end = mid 
        elif(C1 > C2):
            end = mid 
        elif(C2 > C1):
            start = mid 
    return start

alfa1 = 3
alfa2 = -5

def test():
    x0 = 2
    x1 = olverMethod(x0)
    x2 = olverMethod(x1)
    x3 = olverMethod(x2)
    x4 = olverMethod(x3)
    E0 = abs(x0 - alfa1)
    E1 = abs(x1 - alfa1)
    E2 = abs(x2 - alfa1)
    E3 = abs(x3 - alfa1)
    E4 = abs(x4 - alfa1)
    print(E0, E1, E2, E3)
    p = znajdz_p(E1,E2,E3,E4)
    print(p)

def test2():
    x0 = 2
    x1 = olverMethod(x0)
    x2 = olverMethod(x1)
    x3 = olverMethod(x2)
    p = log(abs((x3 - x2) / (x2-x1))) / log((abs((x2-x1)/(x1-x0))))
    print(p)

test2()
