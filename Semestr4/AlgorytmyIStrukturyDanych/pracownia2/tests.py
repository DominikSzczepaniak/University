from copy import deepcopy
n = int(input())

points = []
for i in range(n):
    for j in range(n):
        points.append((i, j))

print(points)


def dynamic_loops(n, current_loop=0, indices=None):
    if indices is None:
        indices = []
    if current_loop < n:
        for i in range(len(points)):
            if i in indices:
                continue
            if len(indices) > 0 and i < indices[len(indices) - 1]:
                continue
            yield from dynamic_loops(n, current_loop + 1, indices + [i])
    else:
        yield indices

id = 0

for i in dynamic_loops(n):
    with open(f'./tests/in{id}.txt', 'w') as f:
        f.write(f'{n}\n')
        for j in i:
            f.write(f'{points[j][0]} {points[j][1]}\n')
        id+=1
