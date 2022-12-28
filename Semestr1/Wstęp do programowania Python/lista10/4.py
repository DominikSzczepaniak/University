# lista = list(map(int, input().split()))
def sumyPodzbiorow(lista, id=0, suma = 0):
    #na kazdym kroku rozpatrujemy obie decyzje odnosnie liczby z listy:
    #brac
    #nie brac
    if(id==len(lista)):
        return [suma]
    sumy1 = sumyPodzbiorow(lista, id+1, suma+lista[id])
    sumy2= sumyPodzbiorow(lista, id+1, suma)
    sumy = [i for i in sumy1+sumy2]
    return sumy
def ciagiNiemalejace(n, A, B, ciag, id=1):
    #na kazdym kroku mozemy wybrac czy chcemy brac liczbe czy nie chcemy brac liczby do obecnego ciagu. zaczniemy z kazdej liczby naturalnej z przedzialu [A, B-n+1] 
    if(id == B+1):
        odpowiedz= [i for i in ciag if len(i) == n]
        return odpowiedz
    nowyciag = [i+[id] for i in ciag]+[i for i in ciag]
    return ciagiNiemalejace(n, A, B, nowyciag, id+1)

lista = {1, 2, 3, 100, 101}
print(set(sorted(sumyPodzbiorow(list(lista)))))

n, A, B = input().split()
n, A, B = int(n), int(A), int(B)
print(sorted(ciagiNiemalejace(n, A, B, [[A], []], A+1)))
