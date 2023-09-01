wyniki = []
for line in open("data.txt"):
    litera = line[0]
    values = []
    for char in line:
        if(char == '.'):
            values.append(".")
        elif(char == '-'):
            values.append("_")
    answer = "".join(values)
    wyniki.append((litera, answer))
wyniki.sort()
for i in range(len(wyniki)):
    print('[(equal? sym "{kod_morse}") "{litera}"]'.format(kod_morse = wyniki[i][1], litera = wyniki[i][0]))