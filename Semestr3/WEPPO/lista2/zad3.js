//1
//(![]+[]) [+[]]
//^ false    ^ miejsce w stringu z +[] czyli 0 bo [] to pusty ciag znakow a + zmienia na liczbe
//wiec mamy false[0] = f


//2
//(![]+[])[+!+[]]
// +! = 1 bo ! ma dlugosc 1 a +[] ma dlugosc 0 wiec suma = 1
// takze false[1] = a

//3
//([![]]+[][[]])[+!+[]+[+[]]]

// ([![]]+[][[]])

// [![]] = tablica z wartoscia false bo [] to true
// [][[]] to udentified 
// [+!+[]+[+[]]] = 1+0+
let a = +!+[] //to jest 1 
let b = [+[]] //to jest tablica [0]
let c = a+b //po dodaniu mamy 1 + [0] a [0] jest zmieniane na ciag znakow wiec mamy '10', a to jest zmieniane na 10 przy odwolywaniu sie do miejsca


//(![]+[])[!+[]+!+[]]

//(![]+[]) to false, juz bylo
//[!+[]+!+[]] = 1+0+1+0 = 2
//false[2] = l

//wiec fail

console.log((![]+[]) [+[]]+ (![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );