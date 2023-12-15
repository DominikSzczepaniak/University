from sympy import symbols, sin, pi
# x = [-1, 0, 2]
# y = [48, -72, 96]
# a)
# def s1(x):
#     return A*x**3 + B*x**2 + C*x + D 

# def s2(x):
#     return E*x**3 + F*x**2 + G*x + H

# def s1prim(x):
#     return 3*A*x**2 + 2*B*x + C

# def s2prim(x):
#     return 3*E*x**2 + 2*F*x + G

# def s1bis(x):
#     return 6*A*x + 2*B

# def s2bis(x):
#     return 6*E*x + 2*F

# s1(-1) = -A + B - C + D = 48
# s1(0) = s2(0) = D = H = -72
# s2(2) = 8*E + 4*F + 2*G + H = 96

# s1prim(0) = s2prim(0) = C = G 

# s1bis(0) = s2bis(0) = 2*B = 2*F

# s1bis(-1) = s2bis(2) = -6*A + 2*B = 12*E + 2*F = 0

A = 34
B = 102
C = -52
D = -72 
E = -17 
F = 102 
G = -52 
H = -72
def s1(x):
    return A * x**3 + B* x**2 + C * x + D
def s1dwa(x):
    return 34 * x**3 - 154*x + 48

print(s1dwa(-1))

def s2(x):
    return E * x**3 + F * x**2 + G * x + H

# print(s1(-1))
# print(s1(0))
# print(s2(0))
# print(s2(2))

# w b) y = 2023x-2024
