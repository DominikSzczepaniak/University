import math as Math
import biblioteka
def f1(x):
    return 2024*x**8 - 1977*x**4 - 1981


def f2(x):
    return 1/(1+x**2)


def f3(x):
    return Math.sin(5*x - Math.pi/3)

print("Funkcja f1:")
for i in range(1, 21):
    print("m = ", i, " ", biblioteka.romberg(f1, -3, 2, i))
print("Funkcja f2:")
for i in range(1, 21):
    print("m = ", i, " ", biblioteka.romberg(f2, -3, 2, i))
print("Funkcja f3:")
for i in range(1, 21):
    print("m = ", i, " ", biblioteka.romberg(f3, -3, 2, i))



