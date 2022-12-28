import turtle 
turtle.tracer(0, 1)
turtle.colormode(255)
def kwadrat(bok, kolor):
    id = []
    liczba = ""
    for i in range(1, len(kolor)-1):
        if(kolor[i] == ','):
            id.append(int(liczba))
            liczba = ""
        else:
            liczba += kolor[i] 
    id.append(int(liczba))
    turtle.begin_fill()
    turtle.fillcolor(id)
    for i in range(4):
        turtle.fd(bok)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(bok) #zeby przejsc do kolejnego pixela po prawej

linie = []
with open("obraz.txt") as f:
    linie = f.readlines()
obraz = []
for wiersz in linie:
    test = wiersz.strip().rsplit()
    obraz.append(test)
obraz2 = [' '] * (len(obraz[0]))
for j in range(len(obraz[0])):
    asd = []
    for i in range(len(obraz)-1, -1, -1):
        asd.append(obraz[i][j])
    obraz2[len(obraz[0])-1-j] = asd
obraz = obraz2

turtle.penup()
turtle.goto(-200,-300)
turtle.pendown()
bok = 10
licznik = 1

        
for i in obraz:
    for j in i:
        kwadrat(bok, j)
    turtle.penup()    
    turtle.goto(-200, -300+licznik*bok)
    turtle.pendown()
    licznik+=1
input()



    
        