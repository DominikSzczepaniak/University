const car = {
    marka: 'Honda',
    model: 'Civic',
    year: 2008
}
console.log(car.year)
let year_string = "year"
console.log(car[year_string])


//Jeśli argumentem operatora "[]" jest liczba, JavaScript traktuje ją jako ciąg znaków i próbuje użyć jej jako nazwy właściwości obiektu. Jeśli nie istnieje właściwość o takiej nazwie, wynik jest "undefined".
const yearProperty = car[2008];
console.log(yearProperty) //undefined

//Jeśli argumentem operatora "[]" jest inny obiekt, JavaScript również przekształca go w ciąg znaków (wykorzystując wynik metody toString() obiektu) i próbuje użyć go jako nazwy właściwości obiektu. W przypadku obiektu "keyObject", jego wartość domyślna to "[object Object]".
const keyObject = {keys: 'year'}
console.log(car[keyObject]) //undefined (brak właściwości o nazwie "[object Object]")


//Programista ma pełną kontrolę nad nazwą klucza, pod którym zapisuje wartość w obiekcie. W obu przypadkach można dowolnie wybierać nazwy kluczy, choć warto zachować ostrożność, aby nie nadpisać istniejących właściwości obiektu.
car[yearProperty] = '10'
console.log(car)

car[keyObject] = "rok"
console.log(car)

const tablica = [1, 2, 3, 4]
console.log(tablica["1"]) //zamieni "1" na 1

const indexObject = {key: "2"}
console.log(tablica[indexObject]) //undefined

tablica["test"] = 1;
console.log(tablica)

console.log(tablica.length)
tablica.length = 2; //elementy nadmiarowe sa obcinane
console.log(tablica)
tablica.length = 5; //elementy ktorych nie ma sa zamieniane na <empty item>
console.log(tablica)