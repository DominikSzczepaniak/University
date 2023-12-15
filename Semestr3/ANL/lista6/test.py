from sympy import symbols, sin, pi

# Funkcja do obliczania wielomianu interpolacyjnego Lagrange'a
def lagrange_interpolation(points):
    x = symbols('x')
    n = len(points)

    # Definicja funkcji f(x)
    f = 2023*x**8 + 1977*x**7 - 1939*x**4 + 1410*x**2 - 966*x + 1996

    # Obliczanie wielomianu interpolacyjnego Lagrange'a
    lagrange_poly = 0
    for i in range(n):
        term = f.subs(x, points[i][0])
        for j in range(n):
            if j != i:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        lagrange_poly += term

    return lagrange_poly

# Punkty interpolacyjne
points = [(-2023, None), (1977, None), (-1945, None), (sin(1), None), (1989, None),
          (-1939, None), (1791, None), (1945, None), (pi, None)]

# Obliczenie wielomianu interpolacyjnego
interpolation_poly = lagrange_interpolation(points)

# Wyświetlenie wyniku
print("Wielomian interpolacyjny:")
print(interpolation_poly)
