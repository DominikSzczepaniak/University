function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);
    return o;
}
const tablica = [1, 2, 3];
var person = {
    a: 12,
    b: 13
}
var personProto = {
    a: 11,
    c: 14
}
Object.setPrototypeOf(person, personProto)
console.log(getLastProto(tablica))
console.log(getLastProto(person))
console.log(getLastProto(personProto))
console.log(getLastProto(person) == getLastProto(personProto))
console.log(getLastProto(person) == getLastProto(tablica))
//wszystko zbiega do null prototype

