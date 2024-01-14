import numpy as np


def simpson(f, a, b, n):
    h = (b - a) / n

    sum_odd = 0
    sum_even = 0

    for i in range(0, n - 1):
        x = a + (i + 1) * h
        if (i + 1) % 2 == 0:
            sum_even += f(x)
        else:
            sum_odd += f(x)

    xi = h / 3 * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))
    return xi


def trapezoidal(f, a, b, n):
    h = (b - a) / n

    sum_x = 0

    for i in range(0, n - 1):
        x = a + (i + 1) * h
        sum_x += f(x)

    xi = h / 2 * (f(a) + 2 * sum_x + f(b))
    return xi


def romberg(f, a, b, n):
    r = np.zeros((n, n))

    #metoda trapezow dla pierwszej kolumny
    h = b - a
    r[0, 0] = 0.5 * h * (f(a) + f(b))

    for i in range(1, n):
        h = 0.5 * h  

        sum_f = 0
        for j in range(1, 2**i, 2):
            x = a + j * h
            sum_f += f(x)
        r[i, 0] = 0.5 * r[i - 1, 0] + h * sum_f

        # Richardson extrapolation 
        for k in range(1, i + 1):
            r[i, k] = r[i, k - 1] + \
                (r[i, k - 1] - r[i - 1, k - 1]) / ((4**k) - 1)

    return float(r[n - 1, n - 1])