function fib(n) {
    if(n == 0){
        return 1;
    }
    if(n == 1){
        return 1;
    }
    return fib(n-1) + fib(n-2);
}
let n = 40;
let wynik = [];
for(let i = 10; i<=n; i++){

    var begin = Date.now();
    let wartosc = fib(i);
    var end = Date.now();
    let czas = (end - begin) / 1000 + " secs";
    //let czas = console.timeEnd();//to wypisuje czas do konsoli, a chce to miec jako wartosc
    wynik.push({n: i, fib: fib(i), time: czas});
}
console.table(wynik);