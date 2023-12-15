import re
import itertools
class SpojnikError(Exception):
    def __init__(self, message="Podano nieprawidlowy spojnik lub nie podano go wcale", *args, **kwargs):
        super().__init__(message, *args, **kwargs)

class ZmiennaError(Exception):
    def __init__(self, id):
        super().__init__("Nie podano wartosci dla zmiennej %s" % id)


class Formula():
    def __init__(self, wyr):
        self.wyr = wyr
        self.formatowanieWejscia()
        self.sparsowaneWyrazenie = self.parse()
    def __add__(self, Formula2):
        return Or(self, Formula2)
    def __mul__(self, Formula2):
        return And(self, Formula2)
    def __str__(self):
        return self.sparsowaneWyrazenie.wypisz()
    #CZESC PARSOWANIA
    def doborSpojnika(self, spojnik, lewo, prawo):
        if spojnik == "^":
            return And(lewo, prawo)
        elif spojnik == "v":
            return Or(lewo, prawo)
        elif spojnik == "->":
            return Impl(lewo, prawo)
        elif spojnik == "<=>":
            return Iff(lewo, prawo)
        elif spojnik == "~":
            return Not(lewo)
        elif spojnik == "T":
            return Prawda()
        elif spojnik == "F":
            return Falsz()
        else:
            raise SpojnikError
            
    def parsowanie(self, wyrazenie):
        # MOZEMY MIEC ALBO WYRAZENIE 
        # X SPOJNIK Y
        # ALBO X
        # X MOZE SIE ZACZYNAC I KONCZYC NAWIASAMI

        # JAK SPRAWDZIC JAKIE WYRAZENIE MAMY?
        # JEŚLI PRZEJDZIEMY PRZEZ CAŁEGO X PATRZAC NA NAWIASY TO NASTEPNY MUSI BYC SPOJNIK - WTEDY MAMY X SPOJNIK Y
        # jesli wyrazenie ma dlugosc 1 to jest to zmienna (oczywiscie oprocz nawiasow)
        # w innym przypadku musi byc spojnik
        if(len(wyrazenie) == 1 and wyrazenie[0] == 'T'):
            return Prawda()
        elif(len(wyrazenie) == 1 and wyrazenie[0] == 'F'):
            return Falsz()
        elif(len(wyrazenie) == 1):
            # print("Dotarlismy do zmiennej %s" % wyrazenie[0])
            return Zmienna(wyrazenie[0])
        elif(len(wyrazenie) == 3 and wyrazenie[0] == '(' and wyrazenie[2] == ')' and wyrazenie[1] == 'T'):
            return Prawda()
        elif(len(wyrazenie) == 3 and wyrazenie[0] == '(' and wyrazenie[2] == ')' and wyrazenie[1] == 'F'):
            return Falsz()
        elif(len(wyrazenie) == 3 and wyrazenie[0] == '(' and wyrazenie[2] == ')'):
            return Zmienna(wyrazenie[1])
        if(len(wyrazenie) == 0):
            raise SpojnikError
        wyrazenie = wyrazenie[1:len(wyrazenie)-1]
        #jesli zdjelismy poczatkowe nawiasy to mamy teraz takie mozliwosci:
        # X SPOJNIK Y
        # gdzie oczywiscie x moze byc otoczony dowolna iloscia nawiasow
        #mamy wiec przypadki dwa:
        #albo X jest otoczony nawiasami albo nie jest
        if(wyrazenie[0] != '('):
            lewa = Zmienna(wyrazenie[0])
            try:
                spojnik = wyrazenie[1]
            except IndexError:
                raise SpojnikError
            prawa = wyrazenie[2:]
            # print("Dotarlismy do zmiennej %s ze spojnikiem %s i pozostala czescia wyrazenia: %s" % (wyrazenie[0], spojnik, prawa))
            return self.doborSpojnika(spojnik, lewa, self.parsowanie(prawa))
        #tutaj X musi byc otoczony nawiasami
        nawias = 1
        it = 1
        lewo = None 
        spojnik = None 
        prawo = None 
        while(nawias > 0):
            if wyrazenie[it+1] == ')':
                nawias-=1
            elif wyrazenie[it+1] == '(':
                nawias += 1
            it+=1
        it+=1
        lewo = wyrazenie[:it]
        if(it >= len(wyrazenie)):
            raise SpojnikError
        spojnik = wyrazenie[it]
        prawo = wyrazenie[it+1:]
        # print("Dotarlismy do zagniezdzonych wyrazen %s \n %s \n %s \n" % (lewo, spojnik, prawo))
        return self.doborSpojnika(spojnik, self.parsowanie(lewo), self.parsowanie(prawo))
    def formatowanieWejscia(self): #splitujemy ze wzgledu na spojniki i nawiasy oraz usuwamy spacje
        separatory = r'(<=>|->| |\^|v|~|\(|\)|T|F)'
        sformatowaneWejscie = [x for x in re.split(separatory, self.wyr) if x and x != " "]
        self.wyr = sformatowaneWejscie 
        self.wyr = ["("] + self.wyr + [")"]
    def parse(self):
        return self.parsowanie(self.wyr)
    #CZESC OBLICZANIA WYNIKU
    # mamy postac typu Klasa lewe prawe
    # wystarczy ze dajemy rekurencje oblicz(lewe) oblicz(prawe) i laczymy wyniki spojnikiem
    # 
    def oblicz(self, zmienne):
        return self.liczenie(zmienne, self.sparsowaneWyrazenie)

    def liczenie(self, zmienne, wyrazenie):
        if(isinstance(wyrazenie, Zmienna)): #przypadek konca rekurencji - zwrocenie zmiennej
            for key in zmienne:
                if(key == wyrazenie.id):
                    return zmienne[key]
            raise ZmiennaError(wyrazenie.id)
        elif(isinstance(wyrazenie, And)):
            return (self.liczenie(zmienne, wyrazenie.left) and self.liczenie(zmienne, wyrazenie.right))
        elif(isinstance(wyrazenie, Or)):
            return (self.liczenie(zmienne, wyrazenie.left) or self.liczenie(zmienne, wyrazenie.right))   
        elif(isinstance(wyrazenie, Not)):
            return (not self.liczenie(zmienne, wyrazenie.left))  
        elif(isinstance(wyrazenie, Impl)):
            lewa = self.liczenie(zmienne, wyrazenie.left)
            prawa = self.liczenie(zmienne, wyrazenie.right)
            if(lewa == True and prawa == False):
                return False
            return True
        elif(isinstance(wyrazenie, Iff)):
            return (self.liczenie(zmienne, wyrazenie.left) == self.liczenie(zmienne, wyrazenie.right))  
        elif(isinstance(wyrazenie, Falsz)):
            return False 
        elif(isinstance(wyrazenie, Prawda)):
            return True 
        
    def getSparsowanaFormula(self):
        return self.sparsowaneWyrazenie
    
    def obliczZmienne(self, wyrazenie):
        if(isinstance(wyrazenie, Zmienna)):
            return wyrazenie.id
        elif(isinstance(wyrazenie, Prawda)):
            return "T"
        elif(isinstance(wyrazenie, Falsz)):
            return "F"
        answer = set()
        answer = answer.union(self.obliczZmienne(wyrazenie.left))
        answer = answer.union(self.obliczZmienne(wyrazenie.right))
        return answer
    
    def tautologia(self):
        return self.Sprawdztautologia(self.sparsowaneWyrazenie)

    def Sprawdztautologia(self, wyrazenie):
        ilosc_zmiennych = self.obliczZmienne(wyrazenie)
        ilosc_zmiennych = [i for i in ilosc_zmiennych]
        permutacje = list(itertools.product([True, False], repeat=len(ilosc_zmiennych)))
        for i in permutacje:
            slownik = dict()
            for k in range(len(ilosc_zmiennych)):
                slownik[ilosc_zmiennych[k]] = i[k]
            wynik = self.oblicz(slownik)
            if(not wynik):
                return False 
        return True
    
    def sprzeczna(self):
        return self.Sprawdzsprzeczna(self.sparsowaneWyrazenie)
            

    def Sprawdzsprzeczna(self, wyrazenie):
        ilosc_zmiennych = self.obliczZmienne(wyrazenie)
        ilosc_zmiennych = [i for i in ilosc_zmiennych]
        permutacje = list(itertools.product([True, False], repeat=len(ilosc_zmiennych)))
        for i in permutacje:
            slownik = dict()
            for k in range(len(ilosc_zmiennych)):
                slownik[ilosc_zmiennych[k]] = i[k]
            wynik = self.oblicz(slownik)
            if(wynik):
                return False 
        return True
    
    def wyliczUproszczenie(self):
        nowyParse = self.wyliczanieUproszczenia(self.sparsowaneWyrazenie)
        self.sparsowaneWyrazenie = nowyParse

    def wyliczanieUproszczenia(self, wyrazenie):
        if(isinstance(wyrazenie, Zmienna)): #przypadek konca rekurencji - zwrocenie zmiennej
            return wyrazenie
        elif(isinstance(wyrazenie, And)):
            if(self.Sprawdzsprzeczna(wyrazenie.left)):
                return Falsz() 
            elif(self.Sprawdzsprzeczna(wyrazenie.right)):
                return Falsz()
            return And(self.wyliczanieUproszczenia(wyrazenie.left), self.wyliczanieUproszczenia(wyrazenie.right))
        elif(isinstance(wyrazenie, Or)):
            if(self.Sprawdztautologia(wyrazenie.left)):
                return Prawda()
            elif(self.Sprawdztautologia(wyrazenie.right)):
                return Prawda()
            return Or(self.wyliczanieUproszczenia(wyrazenie.left), self.wyliczanieUproszczenia(wyrazenie.right))
        elif(isinstance(wyrazenie, Not)):
            return (Not(self.wyliczanieUproszczenia(wyrazenie.left)))  
        elif(isinstance(wyrazenie, Impl)):
            return Impl(self.wyliczanieUproszczenia(wyrazenie.left), self.wyliczanieUproszczenia(wyrazenie.right))
        elif(isinstance(wyrazenie, Iff)):
            return Iff(self.wyliczanieUproszczenia(wyrazenie.left), self.wyliczanieUproszczenia(wyrazenie.right))
        elif(isinstance(wyrazenie, Falsz)):
            return Falsz()
        elif(isinstance(wyrazenie, Prawda)):
            return Prawda()


    licznik = 0
    wyr = None 
    sparsowaneWyrazenie = None
    spojniki = ["^", "v", "->", "<=>", "~", "T", "F"]
    nawiasy = ["(", ")"]

     

class Falsz(Formula):
    def __init__(self):
        pass
    def oblicz(self, zmienne):
        return False
    def wypisz(self):
        return "F"

class Prawda(Formula):
    def __init__(self):
        pass 
    def oblicz(self, zmienne):
        return True
    def wypisz(self):
        return "T"

class Or(Formula):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    def oblicz(self, zmienne:dict): 
        pass
    left = None 
    right = None 
    def wypisz(self):
        return "(" +str(self.left.wypisz()) + ") v (" + str(self.right.wypisz())+ ")"

class And(Formula):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    left = None 
    right = None
    def wypisz(self):
        return "(" +str(self.left.wypisz()) + ") ^ (" + str(self.right.wypisz())+ ")"
        
class Not(Formula):
    def __init__(self, left):
        self.left = left
    left = None 
    def wypisz(self):
        return "(" +"~" + str(self.left.wypisz())+ ")"
        
class Impl(Formula):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    left = None 
    right = None
    def wypisz(self):
       return "(" +str(self.left.wypisz()) + ") -> (" + str(self.right.wypisz())+ ")"

class Iff(Formula):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    left = None 
    right = None
    def wypisz(self):
        return "(" + str(self.left.wypisz()) + ") <=> (" + str(self.right.wypisz()) + ")"

class Zmienna(Formula):
    def __init__(self, id):
        self.id = id
    id = None 
    def wypisz(self):
        return str(self.id)

a = Formula("x -> y")
b = Formula("(x <=> y) v ((x ^ y) ^ (x v y))")
c = Formula("F v T")

print(a)
print(a.oblicz({"x": True, "y": True}))
print(c.tautologia())
print(a.tautologia())

d = Formula("(T v T) v (F v F)")
print("Przed uproszczeniem: ", d)
d.wyliczUproszczenie()
print("Po uproszczeniu: ", d)

# e = Formula("x v y")
# e.oblicz({}) #error nie podano wartosci dla zmiennej x
# f = Formula("x v y v z") #error zle spojniki
