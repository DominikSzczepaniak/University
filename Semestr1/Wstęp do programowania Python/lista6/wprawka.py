def szyfrowanie(haslo, linie):
    licznik = 0
    zaszyfrowane = []
    for litera in linie:
        litera = str(litera)
        xorowane = ord(litera) ^ ord(haslo[licznik])
        zaszyfrowane.append(xorowane)
        licznik += 1
        if(licznik == len(haslo)):
            licznik = 0
    return zaszyfrowane

linie = open("a.txt").read().rsplit()
linie2 = []

for i in linie:
    for j in i:
        linie2.append(j)

haslo = input("Podaj hasło: ")

zaszyfrowane = szyfrowanie(str(haslo), linie2)
wynik = [chr(i) for i in zaszyfrowane]

f = open("wyjscie.txt", "w")
f.write(str(wynik))

odwrocone = szyfrowanie(haslo, wynik)
print("".join([chr(i) for i in odwrocone]))

