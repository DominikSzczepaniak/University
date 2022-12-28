def liczby_pierwsze(n):
    '''Zwraca tablice z wszystkimi liczbami pierwszymi od 2 do n włącznie'''
    #p - jezeli liczba jest liczba pierwsza to ma wartosc 1, jezeli nie jest to ma wartosc 0
    p = [1] * (n+1) 
    p[0]=p[1]=0
    liczby_pierwsze = []
    for i in range(2, n+1):
        if(p[i] == 0): 
            continue
        liczby_pierwsze.append(i)
        for j in range(i+i, n+1, i): #jezeli i byla liczba pierwsza, to wszystkie jej wielokrotnosci nie sa
            p[j] = 0
    return liczby_pierwsze

def dzielniki_pierwsze(n):
    '''Zwraca zbiór dzielników pierwszych liczby n'''
    potencjalne_dzielniki = liczby_pierwsze(n)
    wynik = set()
    for i in potencjalne_dzielniki:
        while(n%i==0):
            n/=i
            wynik.add(i)
    return wynik

print(dzielniki_pierwsze(16))
print(dzielniki_pierwsze(12))
print(dzielniki_pierwsze(10**6+12))