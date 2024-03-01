def tabliczka(x1, x2, y1, y2, skok):
    print("{:<8}".format("x\\y"), end="")
    for y in [round(y, 2) for y in list(float_range(y1, y2, skok))]:
        print("{:<8.2f}".format(y), end="")
    print()

    for x in [round(x, 2) for x in list(float_range(x1, x2, skok))]:
        print("{:<8.2f}".format(x), end="")
        for y in [round(y, 2) for y in list(float_range(y1, y2, skok))]:
            print("{:<8.2f}".format(x * y), end="")
        print()

def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

tabliczka(0.2, 1.3, 0.2, 3.14, 0.15)
