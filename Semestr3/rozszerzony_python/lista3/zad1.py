def najdluzszy_palindrom(tekst):
    najdluzszy = 0
    ans = []
    for i in range(len(tekst)):
        for k in range(i+1, len(tekst)):
            if(tekst[i:k+1] == tekst[i:k+1][::-1]):
                if(najdluzszy < k+1 - i):
                    najdluzszy = k+1 - i
                    ans = []
                    ans.append([i, k])
                elif(najdluzszy == k+1 - i):
                    ans.append([i, k])
    return ans

print(najdluzszy_palindrom("zabccbavtabccba"))
