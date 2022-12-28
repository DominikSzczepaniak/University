def podziel(s):
    '''Funkcja ktora usuwa biale znaki w napisie s'''
    nowy_napis = False
    napis = ""
    wynik = []
    # print(len(napis))
    for i in range(len(s)):
        if(s[i] == " "):
            if(len(napis) > 0):
                wynik.append(napis)
                napis = ""
        else:
            napis += s[i]
    return wynik

s = "   Ala    ma     kota "
print(podziel(s))