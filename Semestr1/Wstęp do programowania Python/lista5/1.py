def F(n):
    if(n%2==0):
        return n // 2
    else:
        return 3*n + 1
    
def energia(n):
    licznik = 1
    while(F(n) != 1):
        licznik+=1
        n = F(n)
    return licznik

def analiza_collatza(a, b):
    wyniki = []
    for i in range(a, b+1):
        wyniki.append(energia(i))
    wyniki = sorted(wyniki)
    mediana = 0
    wielkosc = len(wyniki)
    if(wielkosc%2==0):
        mediana = (wyniki[wielkosc//2] + wyniki[wielkosc//2-1])//2
    else:
        mediana = wyniki[wielkosc//2]
    max_en = wyniki[wielkosc-1]
    min_en = wyniki[0]
    srednia = sum(wyniki) / wielkosc
    return [srednia, mediana, max_en, min_en]
print(energia(7))
print(analiza_collatza(1, 5))
