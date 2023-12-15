import random
def uprosc_tekst(tekst, dl_slowa, liczba_slow):

    nowy_tekst = ""
    for i in tekst.split():
        if(len(i) <= dl_slowa):
            nowy_tekst += i + " "
    do_usuniecia = []
    ile_do_usuniecia = len(nowy_tekst.split()) - liczba_slow
    for i in range(ile_do_usuniecia):
        liczba = random.randint(0, len(nowy_tekst.split())-1)
        while(liczba in do_usuniecia):
            liczba = random.randint(0, len(nowy_tekst.split())-1)
        do_usuniecia.append(liczba)
    wynik = ""
    for i in range(len(nowy_tekst.split())):
        if(i not in do_usuniecia):
            wynik += nowy_tekst.split()[i] + " "
    return wynik

tekst = "Podział peryklinalny inicjałów wrzecionowatych \
   kambium charakteryzuje się ścianą podziałową inicjowaną \
   w płaszczyźnie maksymalnej."
print(uprosc_tekst(tekst, 10, 5))

            
        