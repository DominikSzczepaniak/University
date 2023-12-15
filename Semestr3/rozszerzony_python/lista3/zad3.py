from collections import deque
import numpy as np
def droga(labirynt, miejsce_startowe):
    labirynt = labirynt.splitlines()
    path = []
    visited = set()
    queue = deque()
    queue.append((miejsce_startowe, 0))
    kierunki = ((1, 0), (-1, 0), (0,1),(0,-1))
    odleglosci = np.empty(shape=(len(labirynt), len(labirynt[0])), dtype=int)
    odleglosci.fill(-5)
    odleglosci[miejsce_startowe[0]][miejsce_startowe[1]] = 0
    end_point = (0, 0)
    while queue:
        (current, depth) = queue.popleft()
        odleglosci[current[0]][current[1]] = depth
        visited.add(current)
        if(labirynt[current[0]][current[1]] == "K"):
            end_point = current
            break 
        for i in kierunki:
            next_p = (current[0] + i[0], current[1] + i[1])
            if(next_p[0] < len(labirynt) and next_p[1] < len(labirynt[0]) and next_p not in visited and labirynt[next_p[0]][next_p[1]] != "X"):
                queue.append((next_p, depth+1))
                visited.add(next_p)
    while(end_point != miejsce_startowe):
        path.append(end_point)
        wartosc = odleglosci[end_point[0]][end_point[1]]
        if(wartosc == 0):
            break
        for i in kierunki:
            next_p = (end_point[0]+i[0], end_point[1] + i[1])
            if(next_p[0] < len(labirynt) and next_p[1] < len(labirynt[0]) and odleglosci[next_p[0]][next_p[1]] == wartosc-1):
                end_point = next_p
                break 
    path.append(miejsce_startowe)
    return path
labirynt = """XXXXXX
X....X
X.XXXX
X..X.K
XX...X
XXXXXX
"""
print(droga(labirynt, (1,4)))
labirynt2 = """XXXXXX
X....X
X..X.X
X..X.K
X....X
XXXXXX
"""
print(droga(labirynt2, (4,4)))

#dalem labirynt jako string, ale robie na nim splitlines(), wiec mamy liste stringow (a stringi sa listami, wiec w zasadzie jest to lista list) - latwiej wpisac wielkiego stringa niz listy list ze stringami
