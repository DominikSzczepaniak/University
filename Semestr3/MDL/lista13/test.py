def czymazrodlo(macierz):
    kandydat = 0
    for i in range(1, len(macierz)):
        if(macierz[kandydat][i] == 1 and i != kandydat): #jeśli otrzymamy 1 to możemy wykluczyć wierzchołek i z kandydata 
            continue 
        else:
            kandydat = i 
    sum = 0 
    for i in range(len(macierz)):
        sum += macierz[kandydat][i]
    if(sum == len(macierz) - 1):
        sum = 0
        for i in range(len(macierz)):
            sum += macierz[i][kandydat]
        if(sum == 0):
            return True 
    return False 

macierz = [[0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0]]
print(czymazrodlo(macierz))
            
