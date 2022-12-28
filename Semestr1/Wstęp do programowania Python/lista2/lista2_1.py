def linia_pusto_pelna(n, k):
	for i in range(n):
		print(" "*k, end = "")
		print("#"*k, end = "")

def linia_pelno_pusta(n, k):
	for i in range(n):
		print("#"*k, end = "")
		print(" "*k, end = "")


def szachownica(n, k):
	parzystosc = 0
	for wiersze in range(2*n):
		if(parzystosc%2==0):
			for i in range(k):
				linia_pusto_pelna(n, k)
				print()
			parzystosc+=1
		else:
			for i in range(k):
				linia_pelno_pusta(n, k)
				print()
			parzystosc+=1
		

n, k = map(int, input().split()) 
szachownica(n, k)
