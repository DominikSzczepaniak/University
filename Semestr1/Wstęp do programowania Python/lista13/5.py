#https://drive.google.com/drive/folders/1twa91wzrbuyFNY6k-oHg_Fe0BsTRQS2W
#2017
def prefiks(s, t):
    return (s==t[0:len(s)])
print("PREFIKS:")
print(prefiks("test", "testtest"))
def drabina(L):
    return all([(len(set(L)) == 2 and L[k] != L[k+1]) for k in range(len(L)-1)])
print("DRABINA:")
print(drabina([1,2,2,1]))
print(drabina([1,2,1,2]))
print(drabina([1,2,3,1,2,3]))
print("RYBY:")
def maleRybywDuzych(L):
    return all([(str(sorted(L, key=len)[k]) in str(sorted(L, key=len)[k+1])) for k in range(len(L)-1)])
#["ą"  ,"ć","d" ,"e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n" ,"ń", "o", "ó", "p" ,"r", "s", "ś" ,"t" ,"u" ,"w" ,"y" ,"z" ,"ź" ,"ż"] 
print(maleRybywDuzych(["rekinisko", "rekin", "eki", "megarekinisko", "megarekiniskozilla"]))
def poltaksowkowa(N):
    return max([(i*i*i+j*j*j==N) for i in range(N+1) for j in range(N+1)])
print("Poltaksowkowa:")
print(poltaksowkowa(7))
print(poltaksowkowa(8))
print(poltaksowkowa(9))