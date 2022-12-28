def koperta(n):
	A = []
	A.append(["*"]*(2*n+1))
	ile = 0
	for i in range(1, 2*n):
		if(i == n):
			tab = ["*"]
			for j in range(n-1):
				tab.append(" ")
			tab.append("*")
			for j in range(n-1):
				tab.append(" ")
			tab.append("*")
			A.append(tab)
			ile = ile-1
		else:
			if(i < n):
				tab = ["*"]
				for j in range(ile):
					tab.append(" ")
				tab.append("*")
				zostalo = 2*n+1 - 2 - ile*2 - 2
				for j in range(zostalo):
					tab.append(" ")
				tab.append("*")
				for j in range(ile):
					tab.append(" ")
				tab.append("*")
				A.append(tab)
				ile = ile + 1
			else:
				tab = ["*"]
				for j in range(ile):
					tab.append(" ")
				tab.append("*")
				zostalo = 2*n+1 - 2 - ile*2 - 2
				for j in range(zostalo):
					tab.append(" ")
				tab.append("*")
				for j in range(ile):
					tab.append(" ")
				tab.append("*")
				A.append(tab)
				ile = ile - 1
	A.append(["*"]*(2*n+1))
	for i in A:
		for j in i:
			print(j, end = "")
		print()


#n=3
#0*******
#1**   **
#2* * * *
#3*  *

n = int(input())
koperta(n)
