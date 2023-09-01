for line in open("data.txt"):
    litera = line[0]
    values = []
    for char in line:
        if(char == '.'):
            values.append("#\.")
        elif(char == '-'):
            values.append("#\_")
    answer = " ".join(values)
    print("(make_string (list {ans})) ;{lit}".format(ans = answer, lit = litera))
    #(make_string (list #\_ #\. #\. #\.) "")
