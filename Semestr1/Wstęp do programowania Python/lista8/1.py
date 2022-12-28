import random
from collections import defaultdict as dd

pol_ang = dd(lambda:[])
popularnosc = dd(lambda:0)
for line in open("brown.txt"):
    for slowo in line.rsplit():
        popularnosc[slowo] += 1

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)
    
def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            najpopularniejsze = 0
            taka_sama_popularnosc = []
            for slowo in pol_ang[s]:
                if(popularnosc[slowo] > najpopularniejsze):
                    najpopularniejsze = popularnosc[slowo]
                    taka_sama_popularnosc = [slowo]
                elif(popularnosc[slowo] == najpopularniejsze):
                    taka_sama_popularnosc.append(slowo) 
            wynik.append(random.choice(taka_sama_popularnosc))
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

for i in range(15):
    print (tlumacz(zdanie))            
            
