def is_prime(n):
    if(n == 1):
        return False
    i = 2
    while(i*i <= n):
        if(n%i == 0):
            return False
        i = i+1
    return True
wynik = 0
for i in range(1, 100001):
    if(is_prime(i) and "777" in str(i)):
        print(i)
        wynik = wynik + 1
print(wynik)

