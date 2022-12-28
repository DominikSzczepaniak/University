wiersze = []
for line in open("lalkaTOM1.txt"):
    if(line.rsplit()):
        wiersze.append(line.rsplit())
# print(wiersze)
maxdlugosc = 0
maxfragment = []
dlugosc = 0
fragment = []
for linijki in wiersze:
    for slowa in linijki:
        polska_litera = False 
        for litera in slowa:
            if(ord(litera) > 127):
                polska_litera = True 
        if(polska_litera == False):
            fragment.append(slowa)
            for litera in slowa:
                if((ord(litera) >=97 and ord(litera) <= 122) or (ord(litera) >= 65 and ord(litera) <= 90)):
                    dlugosc += 1
        else:
            if(dlugosc > maxdlugosc):
                maxfragment = fragment
                fragment = []
                maxdlugosc = dlugosc
                dlugosc = 0
                # print(" ".join(maxfragment)) # zmiany w trakcie programu, nic nie widac, bo teksty za dlugie
print(maxdlugosc)
print(" ".join(maxfragment))




