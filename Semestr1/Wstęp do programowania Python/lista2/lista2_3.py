def kolko(n, dodac):
	szerokosc = n*2+1
	#linie od poczatku do koncowej
	for i in range(1, n+1):
		for puste in range(dodac):
			print(" ", end = "")
		grubosc = 2*i+1
		wolnych = szerokosc-grubosc
		for puste in range(wolnych//2):
			print(" ", end = "")
		for kratki in range(grubosc):
			print("#", end = "")
		for puste in range(wolnych//2):
			print(" ", end = "")
		print()
	#srodkowa linia
	for puste in range(dodac):
		print(" ", end = "")
	for i in range(szerokosc):
		print("#", end = "")
	print()	
	for i in range(n, 0, -1):
		for puste in range(dodac):
			print(" ", end = "")
		grubosc = 2*i+1
		wolnych = szerokosc-grubosc
		for puste in range(wolnych//2):
			print(" ", end = "")
		for kratki in range(grubosc):
			print("#", end = "")
		for puste in range(wolnych//2):
			print(" ", end = "")
		print()

n = int(input())
dodac = 2
for i in range(n, n+3):
	kolko(i, dodac)
	dodac-=1 

