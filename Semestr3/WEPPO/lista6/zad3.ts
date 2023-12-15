function forEach<T>(a: T[], f: (t: T) => void): void{ 
    for (let i = 0; i < a.length; i++) {
        f(a[i]);
    }
}
function map<T>(a: T[], f: (t: T) => T): T[]{
    for(var i = 0; i<a.length; i++){
        a[i] = f(a[i]);
    }
    return a;
}
function filter<T>(a: T[], f: (t: T) => boolean): T[]{
    let wynik: T[] = [];
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