def pierwsza_imperatywna(n):
    pierwsze = [True] * (n+1)
    pierwsze[0] = pierwsze[1] = False 
    for i in range(2, n+1):
        if pierwsze[i]:
            for j in range(i*i, n+1, i):
                pierwsze[j] = False
    #return [i for i in range(n+1) if pierwsze[i]] #nie wiem czy to moge tu uzyc ale to bym uzyl
    odpowiedz = []
    for i in range(2, n+1):
        if(pierwsze[i]):
            odpowiedz.append(i)
    return odpowiedz 

def pierwsza_skladana(n):
    return [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, i))]    

def pierwsza_funkcyjna(n):
    return list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, n+1)))

print(pierwsza_funkcyjna(111))
print(pierwsza_imperatywna(111))
print(pierwsza_skladana(111))