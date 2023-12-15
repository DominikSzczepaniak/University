from math import log 
#|E_{n+1} ~ C*|E_n|^p
# r3 = C*r2^p
# r2 = C*r1^p
# r1 = C*r0^p

def znajdz_p(r0, r1,r2,r3):
    start = 1
    end = 25 
    licznik = 0
    while(start < end):
        licznik+=1
        if(licznik > 50):
            break
        mid = (start+end)/2
        C1 = r3/r2**mid
        C2 = r2/r1**mid
        C3 = r1/r0**mid
        if(abs(C1-C2) < 1e-3):
            start = mid 
            end = mid 
        elif(C1 > C3):
            end = mid 
        elif(C3 > C1):
            start = mid 
    return start

r0 = 0.763907023
r1 = 0.543852762
r2 = 0.196247370
r3 = 0.009220859
p1 = znajdz_p(r0,r1,r2,r3)
licznik = 0
wartosc = r3 
C1 = r2/r1**p1
while(wartosc > 1e-100):
    wartosc = C1 * wartosc ** p1
    # print(wartosc)
    licznik+=1
print("r ~~ ", licznik+4)



a0 = 0.605426053
a1 = 0.055322784
a2 = 0.004819076
a3 = 0.000399783
p2 = znajdz_p(a0, a1,a2,a3)
C2 = a2/a1**p2
licznik = 0
wartosc = a3 
while(wartosc > 1e-100):
    wartosc = C2 * wartosc ** p2
    # print(wartosc)
    licznik+=1
print("a ~~ ", licznik+4)