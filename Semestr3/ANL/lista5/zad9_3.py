import sys
from math import log, sin, cos
def Olver(f, dfdx, dfdfdx, x, eps, return_x_list=False):
    f_value = f(x)
    iteration_counter = 0
    if return_x_list:
        x_list = []

    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f(x)/dfdx(x) - 1/2 * (dfdfdx(x)/dfdx(x)) * (f(x)/dfdx(x))**2
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     

        f_value = f(x)
        iteration_counter += 1
        if return_x_list:
            x_list.append(x)

    # solution found or too many iterations
    if abs(f_value) > eps:
        iteration_counter = -1  # lack of convergence

    if return_x_list:
        return x_list, iteration_counter
    else:
        return x, iteration_counter
    

def f(x):
    return x**3 + 7*x**2 - 5*x - 75
def dfdx(x):
    return 3*x**2 + 14*x - 5
def dfdfdx(x):
    return 6*x + 14

def g(x):
    return x**4 + 5*x**3 - 5*x**2 - 75*x
def dgdx(x):
    return 4*x**3 + 15*x**2 - 10*x - 75
def dgdgdx(x):
    return 12*x**2 + 30*x - 10

def h(x):
    return x**7 + 5*x**6 - 5*x**5 - 75*x**4
def dhdx(x):
    return 7*x**6 + 30*x**5 - 25*x**4 - 300*x**3
def dhdhdx(x):
    return 42*x**5 + 150*x**4 - 100*x**3 - 900*x**2

    

x, iter = Olver(f, dfdx, dfdfdx, x=1000, eps=1e-6, return_x_list=True)
x2, iter = Olver(g, dgdx, dgdgdx, x=1000, eps=1e-6, return_x_list=True)
x3, iter = Olver(h, dhdx, dhdhdx, x=1000, eps=1e-6, return_x_list=True)
print(x)
def rate(x, x_exact):
    e = [abs(x_ - x_exact) for x_ in x]
    q = [log(e[n+1]/e[n])/log(e[n]/e[n-1])
         for n in range(1, len(e)-1, 1)]
    return q

def print_rates(method, x, x_exact):
    q = ['%.2f' % q_ for q_ in rate(x, x_exact)]
    print(method + ':')
    for q_ in q:
        print(q_),
    print()

print_rates('Olver', x, -5)
print_rates('Olver2', x2, 3)
print_rates('Olver3', x3, 3)
