#zachowac miejsce pierwszego wystapienia
def usun_duplikaty(L):
	L = [[liczba, miejsce+1] for miejsce, liczba in enumerate(L)]
	L = sorted(L)
	bez_duplikatow = []
	bez_duplikatow.append(L[0])
	for i in range(1, len(L)):
		if(bez_duplikatow[len(bez_duplikatow)-1][0] != L[i][0]):
			bez_duplikatow.append(L[i])
	wynik = [[i[1], i[0]] for i in bez_duplikatow]
	wynik = sorted(wynik)
	wynik2 = [i[1] for i in wynik]
	return wynik2



tab = list(map(int, input().split()))
print(usun_duplikaty(tab))

