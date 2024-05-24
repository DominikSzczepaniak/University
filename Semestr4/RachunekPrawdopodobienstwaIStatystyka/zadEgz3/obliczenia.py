from math import e

a = [3, 4, 6, 10]

markov = lambda a, l: 1/(l*l*a)
chebyshev = lambda a, l: 1/((l*l*a-1)**2)
chernoff = lambda a, l: a * l*l * e**(-(l*l)*a + 1)
exact = lambda a, l:  e**(-l*l*a)
lambdaa = 12
for i in a:
    print(chebyshev(i, lambdaa))
