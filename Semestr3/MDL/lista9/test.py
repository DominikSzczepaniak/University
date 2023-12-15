G = [[], [2], [1, 3, 5], [2, 4, 6], [3, 7], [2, 9], [3, 8], [4], [6, 10], [5], [8, 11], [10]]
n = 11
def dfs(start, odl, visited):
    visited[start] = True
    for i in G[start]:
        if(not visited[i]):
            odl[i] = odl[start]+1 
            visited[i] = True
            dfs(i, odl, visited)
def wierzcholek_centralny():
    visited = [False] * (n+1)
    odl = [0] * (n+1)
    dfs(1, odl, visited)
    maxV = 0
    vert = 1
    for i in range(2, n+1):
        if(maxV < odl[i]):
            maxV = odl[i]
            vert = i
    odl = [0] * (n+1)
    visited = [False] * (n+1) #resetujemy pod nowy dfs odl i visited
    dfs(vert, odl, visited)
    print(vert, odl)
    d = 0 
    for i in range(1, n+1):
        d = max(d, odl[i])
    szuk = d//2
    if(d%2==0): #jeden wierzcholek 
        for i in range(1, n+1):
            if(odl[i] == szuk):
                return i    
    else: #dwa wierzcholki 
        odl2 = [0] * (n+1)
        visited = [False] * (n+1)
        maxV = 0
        vert = 1
        for i in range(1, n+1):
            if(maxV < odl[i]):
                maxV = odl[i]
                vert = i
        dfs(vert, odl2, visited)
        wynik = []
        print(vert, odl2)

        for i in range(1, n+1):
            if(odl[i] == szuk and (odl2[i] == szuk-1 or odl2[i] == szuk+1)):
                wynik.append(i)
        for i in range(1, n+1):
            if(odl2[i] == szuk and (odl[i] == szuk-1 or odl[i] == szuk+1)):
                wynik.append(i)
        return sorted(wynik)
    
print(wierzcholek_centralny())