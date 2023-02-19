#https://drive.google.com/drive/folders/1twa91wzrbuyFNY6k-oHg_Fe0BsTRQS2W
#2019
def zrob_tytul(s):
    return [i[0].upper()+i[1:] for i in s.split()]
print(zrob_tytul("test nazwy ksiazki"))
def suma_jednocyfrowych(L):
    return sum([i for i in L if len(str(i)) == 1])
print(suma_jednocyfrowych([123, 12, 1, 3, 4, 5, 124124]))
def same_palindromy(L):
    return all([i == i[::-1] for i in L])
print(same_palindromy(["teet", "asddsa", "qwertyytrewq"]))