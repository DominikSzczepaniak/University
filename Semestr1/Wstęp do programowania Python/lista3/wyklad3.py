def rysowanie_rozety():
    from turtle import speed, pensize, fd, rt, bk
    import random
    speed('fastest')
    pensize(2)
    def kwadrat(n):
        for i in range(4):
            fd(n)
            rt(90)

    def rozeta(a, b, n):
        for i in range(n):
            fd(a)
            kwadrat(b)
            bk(a)
            rt(360/n)
    rozeta(20, 10, 6)
    rozeta(50, 20, 6)
    input("a")

def usuwanie_cyfr_z_napisu():
    import random
    def safe_int(d):
        try:
            return int(d)
        except ValueError:
            return None
    def jest_cyfra(d):
        return ord(d) >= 48 and ord(d) <= 57 
    def jest_cyfra(d):
        return d in '0123456789'
    def jest_cyfra(d): 
        return safe_int(d) in range(10)
    def jest_cyfra(d): 
        return safe_int(d) in [0,1,2,3,4,5,6,7,8,9]
    def jest_cyfra(d): 
        return d.isdigit()
    def jest_cyfra(d):
        return '0' <= d <= '9'
    def usun_cyfry(napis):
        wynik = ''
        for a in napis:
            if(jest_cyfra(a)):
                wynik += '*'
            else:
                wynik += a
        return wynik
    print(usun_cyfry("Ala ma 3 koty i 27 kanarków"))
usuwanie_cyfr_z_napisu()

#1. importowanie do funkcji -------- globalnie
#2. zlozonosc czasowa try: except: ------- nie wykonujemy tego do trywialnych ooperacji tylko czesciej do globalnych ktore sa rzadko