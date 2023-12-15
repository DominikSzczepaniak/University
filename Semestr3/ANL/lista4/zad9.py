# d/dx f(x)^(1/r) = 1/r * f(x)^(1/r - 1) * f'(x)


def f(x):
    return (x-6)**6

def df(x):
    return 6*(x-6)**5

x1 = 121234
r = 6
for i in range(1):
    x1 = x1 - (r*f(x1) / df(x1))

print("Metoda z zadania: ", x1)
    