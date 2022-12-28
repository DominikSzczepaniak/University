slowa = set(open("popularne_slowa.txt", "r").read().rsplit('\n'))
uzyte = set()
for i in slowa:
    if(i in uzyte or i[::-1] in uzyte):
        continue 
    if(i[::-1] in slowa):
        print(i, i[::-1])
        uzyte.add(i)
        uzyte.add(i[::-1])

