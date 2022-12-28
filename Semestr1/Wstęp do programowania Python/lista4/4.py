def sito_erasthothenesa(n):
	pierwsze = [1]*(n+1)
	pierwsze[0] = pierwsze[1] = 0
	#liczby_pierwsze = []
	for i in range(2, n+1):
		if(pierwsze[i] == False):
			continue
		for j in range(i+i, n+1, i):
			pierwsze[j] = 0
	return pierwsze

def is_palindrom(n):
	n = str(n)
	for i in range(len(n)//2):
		if(n[i] != n[len(n)-1-i]):
			return False
	return True

def palindromiczne_liczby_pierwsze(n, p):
	if(p[n] == 1 and is_palindrom(n)):
		return True
	return False

def palindrom(a, b):
	pierwsze = sito_erasthothenesa(b)
	lista = []
	for liczba in range(a, b+1):
		if(palindromiczne_liczby_pierwsze(liczba, pierwsze) == True):
			lista.append(liczba)
	return lista

print(palindrom(10, 200))	
