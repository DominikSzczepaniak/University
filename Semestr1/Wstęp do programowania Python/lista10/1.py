from collections import defaultdict
tekst = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
kod_ascii_litera = defaultdict(lambda: 0)
kod_ascii_wartosc = defaultdict(lambda: 0)
licznik = 0
for litera in tekst:
    kod_ascii_litera[litera] = licznik
    kod_ascii_wartosc[licznik] = litera
    licznik += 1
def cesar(s, k):
    wynik = ""
    for litera in s:
        wartosc = kod_ascii_litera[litera]
        wartosc = (wartosc+k)%len(tekst)
        wynik += kod_ascii_wartosc[wartosc]
    return wynik 

ciphered = cesar(input().strip(),7)
deciph = cesar(ciphered, -7)
print(ciphered)
print(deciph)
