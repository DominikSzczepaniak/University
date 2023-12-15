function sum(...args){
    var wynik = 0;
    for(var i = 0; i<args.length; i++){
        wynik += args[i];
    }
    return wynik;
}

console.log(sum(1,2,3));