def slowo_na_slownik(s):
    slownik = dict()
    for i in s:
        if i not in slownik:
            slownik[i] = 0
        slownik[str(i)] += 1
    return slownik 
def ukladable(slowo1, slowo2):
    slownik1 = slowo_na_slownik(slowo1)
    slownik2 = slowo_na_slownik(slowo2)
    for keys in slownik1:
        if(slownik2[keys] < slownik1[keys]):
            return False 
    return True 
slowo1 = input()
slowo2 = input()
print(ukladable(slowo1, slowo2))
