from losowanie_fragmentow import losuj_fragment 

def silnia(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

def krzyzyk(n):
	for j in range(n):
		print(" "*n + "*"*n + " "*n, end = "")
		print("")

	for j in range(n):
		print("*"*(3*n), end = "")
		print("")
		
	for j in range(n):
		print(" "*n + "*"*n + " "*n, end = "")
		print()

def losuj_haslo(n):
	dlugosc = 0
	haslo = ""
	while(dlugosc < n):
		fragment = losuj_fragment()
		if(len(fragment) + dlugosc <= n and len(fragment)+dlugosc != n-1):
			haslo = haslo + fragment
			dlugosc += len(fragment)
	return haslo



print(silnia(4))
for i in range(4, 101):
	ilecyfr = len(str(silnia(i)))
	if(ilecyfr >= 10 and ilecyfr <= 20):
		print("{0}! ma {1} cyfr".format(str(i), ilecyfr))
		continue
	if((ilecyfr%10 >= 5 and ilecyfr%10 <= 9) or(ilecyfr%10==1)):
		print("{0}! ma {1} cyfr".format(str(i), ilecyfr))
		continue
	else:
		print("{0}! ma {1} cyfry".format(str(i), ilecyfr))
		continue

krzyzyk(4) 
for i in range(10):
	print(losuj_haslo(8))
for i in range(10):
	print(losuj_haslo(12))

