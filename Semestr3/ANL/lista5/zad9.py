from math import log

#f(~14.929) = 0
#f(2) = 0
def f(x):
    return x**4 - 16*x**3 + 16*x**2 - 4*x + 56

def fPrim(x):
    return 3*x**2 - 2

def fDoublePrim(x):
    return 6*x


def g(x):
    return x**4 + 5*x**3 - 5*x**2 - 75*x
def dgdx(x):
    return 4*x**3 + 15*x**2 - 10*x - 75
def dgdgdx(x):
    return 12*x**2 + 30*x - 10

def metodaOlvera(xn, f, fPrim, fDoublePrim):
    return xn -  f(xn)/fPrim(xn) - 1/2 * (fDoublePrim(xn)/fPrim(xn)) * (f(xn)/fPrim(xn))**2


def test(x0, f, fPrim, fDoublePrim):
    xnm2 = x0
    xnm1 = metodaOlvera(xnm2, f, fPrim, fDoublePrim)
    xn = metodaOlvera(xnm1, f, fPrim, fDoublePrim)
    xnw1 = metodaOlvera(xn, f, fPrim, fDoublePrim)
    q = log(abs((xnw1 - xn) / (xn-xnm1))) / log((abs((xn-xnm1)/(xnm1-xnm2))))
    print(q) 
    #także q to 3
    #https://en.wikipedia.org/wiki/Rate_of_convergence
    #order estimation


test(14, f, fPrim, fDoublePrim)
test(3, g, dgdx, dgdgdx)
