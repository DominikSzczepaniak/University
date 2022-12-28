from math import sqrt
# crop((min,max), list): zwraca listę wszystkich wartości z list, ale przyciętą do odpowiednich wartosci min i max, np. crop([1,4],[3,4,5,100,2,-200]) powinno zwrócić [3,4,4,4,2,1]. Twoje rozwiązanie powinno zawierać dodatkowy inny test, najlepiej z wartościami zmiennoprzecinkowymi.
def crop(minmax, list):
    return [minmax[0] if i < minmax[0] else minmax[1] if i > minmax[1] else i for i in list]
print(crop([1,4], [3,4,5,100,2,-200]))
# test z przykladu



# in_rectange( (x1,y1),(x2,y2), list), gdzie list jest listą punktów (jak [(x,y),(x',y'), ...] ) , a (x1,y1) i (x2,y2) określają odpowienio lewy dolny i prawy górny róg prostokąta, powinno zwrócić listę wartości true i false, w zależności czy punkt znajduje się w prostokącie czy nie.
def in_rectange(p1, p2, list):
    return [(i[0] <= p2[0]) and (i[0] >= p1[0]) and (i[1] <= p2[1]) and (i[1] >= p1[1]) for i in list]
print(in_rectange((1,2), (4, 5), [(1,2),(5,6),(7,9),(5,1),(5, 4), (9, 5)]))
#kwadrat 
#.0123456789
#0..........
#1.....X....
#2.####.....
#3.####.....
#4.####X....
#5.####....X
#6.....X....
#7..........
#8..........
#9.......X..


# dist((x,y),list): zamienia listę punktów na listę ich odległości od zadalego punktu
def dist(p, list):
    return [sqrt((i[0]-p[0])**2+(i[1]-p[1])**2) for i in list]
print(dist((1,2), [(3, 4), (4, 2), (5, 6), (7, 4), (8, 2), (9, 1)]))
#punkt (1,2)
#a) sqrt(2^2+2^2)=sqrt(8) troche mniej niz 3
#b) sqrt(3^2) = 3
#c) sqrt(4^2+4^2) = sqrt(32) troche mniej niz 6 i troche wiecej niz 5.5
#d) sqrt(6^2+2^2) = sqrt(40) troche mniej niz 6.5 i troche wiecej niz 6
#e) sqrt(7^2) = 7
#f) sqrt(8^2+1^2) = sqrt(65) troche wiecej niz 8
 


# sortpts((x,y),list): zwraca listę posortowanych po dystansie punktów z listy, z dodanymi do niech dystansami jak np: [((1,5),4.76),((4,7),7.89), ... ].
def sortpts(p, list):
    return[ [i[1], i[0]] for i in 
            sorted([ (sqrt(  ((p[0]-punkt[0])**2) + ((p[1]-punkt[1])**2)  ) , punkt) 
                for punkt in list]) ]
print(sortpts((1,2), [(1, 10), (1, 8), (1, 9), (5, 4), (6, 7), (11, 5)]))
#5a) sqrt(8^2) = 8
#2b) sqrt(6^2) = 6
#3c) sqrt(7^2) = 7
#1d) sqrt(4^2+2^2) = sqrt(20) = troche wiecej niz 4 i mniej niz 4.5
#4e) sqrt(5^2+5^2) = sqrt(50) = troche wiecej niz 7
#6f) sqrt(10^2+3^2) = sqrt(109) = troche wiecej niz 10 i mniej niz 10.5
 