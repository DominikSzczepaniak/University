let ilosc = 0;
for(let i = 0; i<100000; i++){
    let napis = i.toString();
    let suma = 0;
    for(let j = 0; j<napis.length; j++){
        if(i % parseInt(napis[j]) != 0){
            continue;
        }
        suma += parseInt(napis[j]);
    }
    if(i % suma == 0){
        ilosc++;
    }
}
console.log(ilosc);
//czemu przegladarka rzuca blad przy var, a nodejs nie?