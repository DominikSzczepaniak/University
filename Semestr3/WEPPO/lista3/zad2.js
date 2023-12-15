function forEach(a, f){
    f(a);
}
function map(a, f){
    for(var i = 0; i<a.length; i++){
        a[i] = f(a[i]);
    }
    return a;
}
function filter(a, f){
    const wynik = []
    for(var i = 0; i<a.length; i++){
        if(f(a[i])){
            wynik.push(a[i]);
        }
    }
    return wynik;
}
const l = [1, 2, 3, 4];
forEach(l, _ => {console.log( _ ); });
console.log(filter(l, _ => _ < 3));
console.log(map(l, _ => _ * 2));