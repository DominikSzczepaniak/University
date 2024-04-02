import sys 

testNr = sys.argv[1]
obwod = 0

def odleglosc(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def obwodLicz(p1, p2, p3):
    return odleglosc(p1, p2) + odleglosc(p2, p3) + odleglosc(p3, p1)
punkty1 = []
with open('out' + testNr, 'r') as f:
    p1a, p1b = f.readline().split()
    p2a, p2b = f.readline().split()
    p3a, p3b = f.readline().split()
    punkty1.append((int(p1a), int(p1b)))
    punkty1.append((int(p2a), int(p2b)))
    punkty1.append((int(p3a), int(p3b)))
    #calculate circuit of those points
    obwod = obwodLicz((int(p1a), int(p1b)), (int(p2a), int(p2b)), (int(p3a), int(p3b)))
obwod2 = 0
punkty2 = []
with open('out/out' + testNr + '.txt', 'r') as f:
    p1a, p1b = f.readline().split()
    p2a, p2b = f.readline().split()
    p3a, p3b = f.readline().split()
    punkty2.append((int(p1a), int(p1b)))
    punkty2.append((int(p2a), int(p2b)))
    punkty2.append((int(p3a), int(p3b)))
                
    #calculate circuit of those points
    obwod2 = obwodLicz((int(p1a), int(p1b)), (int(p2a), int(p2b)), (int(p3a), int(p3b)))

if obwod != obwod2:
    print("Źle test " + testNr, obwod, obwod2, punkty1, punkty2)