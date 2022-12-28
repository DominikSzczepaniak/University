from collections import defaultdict as dd
imie_nazwisko = input("Wpisz imie i nazwisko:")
litery_w_imieniu_i_nazwisku = dd(lambda:0)
for czlony in imie_nazwisko.rsplit():
    for litery in czlony:
        litery_w_imieniu_i_nazwisku[litery]+=1
rozlozenie_slow_na_litery = dd(lambda:dd(0))
id = []
for line in open("popularne_slowa.txt"):
    for slowo in line.rsplit():
        id.append(slowo)
        wyraz = dd(lambda: 0)
        for litera in slowo:
            wyraz[litera] += 1
        rozlozenie_slow_na_litery[slowo] = wyraz 

uzyte = set()
for id1 in range(len(id)):
    wyjsc = False 
    literki1 = dd(lambda: 0)
    for litera,ilosc in rozlozenie_slow_na_litery[id[id1]].items():
        literki1[litera] += ilosc
        if(ilosc > litery_w_imieniu_i_nazwisku[litera]):
            # print(ilosc, litery_w_imieniu_i_nazwisku[litera])
            wyjsc = True 
            break
    if(wyjsc == False):
        for id2 in range(len(id)):
            if(id1 == id2):
                continue 
            if(  (id[id1] , id[id2]) in uzyte or (id[id1],id[id2]) in uzyte):
                continue 
            for litera,ilosc in rozlozenie_slow_na_litery[id[id2]].items():
                literki1[litera] += ilosc
                if(literki1[litera] > litery_w_imieniu_i_nazwisku[litera]):
                    wyjsc = True 
                    break
            if(wyjsc):
                continue
            for litera, ilosc in literki1.items():
                if(ilosc != litery_w_imieniu_i_nazwisku[litera]):
                    wyjsc = True
                    break 
            if(wyjsc):
                continue 
            print(id[id1], id[id2])
            uzyte.add( (id[id1], id[id2]) )
            uzyte.add( (id[id2], id[id1]) )
                