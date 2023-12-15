ile = 0
for i in {"0", "1", "2"}:
    for j in {"0", "1", "2"}:
        for k in {"0", "1", "2"}:
            for l in {"0", "1", "2"}:
                if(i == j and (i == "1" or i == "0")):
                    continue 
                if(j == k and (j == "1" or j == "0")):
                    continue
                if(k == l and (k == "1" or k == "0")):
                    continue
                ile+=1
                print(i,j,k)
print(ile)