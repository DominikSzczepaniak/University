def usun_w_nawiasach(s):
    nowy_napis = ""
    otwarcie_nawiasu = 0
    for i in s:
        if(i=="("):
            otwarcie_nawiasu += 1
        if(otwarcie_nawiasu == 0):
            nowy_napis = nowy_napis + i
        if(i==")"):
            otwarcie_nawiasu -= 1
    return nowy_napis


napis = input()
print(usun_w_nawiasach(napis))
