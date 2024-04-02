import sys

def my_check(my_output, dif_output):
    my_points = [tuple(map(int, line.split())) for line in my_output]
    dif_points = [tuple(map(int, line.split())) for line in dif_output]

    if len(my_points) != 3 or len(dif_points) != 3:
        print("Invalid number of points.")
        return False

    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    def param(p1, p2, p3):
        a = distance(p1, p2)
        b = distance(p2, p3)
        c = distance(p3, p1)
        return a + b + c
    
    my_param = param(*my_points)
    dif_param = param(*dif_points)

    if abs(my_param - dif_param) > 1e-3:
        print(f"Invalid perimeter my != dif: {my_param} != {dif_param}")
        return False
    
    return True

my_check(sys.argv[1], sys.argv[2])