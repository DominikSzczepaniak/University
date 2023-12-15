import matplotlib 
import numpy
from matplotlib import pyplot

def zwykle(ilosc_wezlow=100, ilosc_x = 1000):
    def p(x, wezly):
        wynik = 1.0
        for i in range(len(wezly)):
            wynik *= (x - wezly[i])
        return wynik
    x_values = numpy.linspace(-1, 1, ilosc_x) 
    wezly = numpy.linspace(-1, 1, ilosc_wezlow)
    y_values = [p(x, wezly) for x in x_values]
    return x_values, y_values

def chebyshevowe(ilosc_wezlow=100, ilosc_x=1000):
    def chebyshev_nodes(n):
        k_values = numpy.arange(n + 1)
        nodes = numpy.cos((2 * k_values + 1) * numpy.pi / (2 * n + 2))
        return nodes

    def calculate_polynomial(x, nodes):
        result = 1.0
        for node in nodes:
            result *= (x - node)
        return result

    def plot_polynomials():
        x_values = numpy.linspace(-1, 1, ilosc_x)
        
        nodes = chebyshev_nodes(ilosc_wezlow)
        y_values = [calculate_polynomial(x, nodes) for x in x_values]
        return x_values, y_values
    return plot_polynomials()

wezly = [10, 30, 60, 100]
xy = [30, 50, 100, 1000]
for i in range(len(wezly)):
    x1, y1 = chebyshevowe(wezly[i], xy[i])
    x2, y2 = zwykle(wezly[i], xy[i])
    plot1, plot2 = matplotlib.pyplot.subplots(2)
    plot2[0].plot(x1, y1, label='chebyshevowe')
    plot2[1].plot(x2, y2, label='zwykle')
    matplotlib.pyplot.show()



#na końcach przedziału wielomian interpolacyjny, jeśli węzły są równoodległe nie jest poprawny. To pokazuje chyba jak ważny jest dobiór węzłów