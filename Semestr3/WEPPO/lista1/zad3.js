let ilosc = 0;
for(let i = 2; i<100001; i++){
    let pierwsza = true;
    for(let j = 2; j*j<i; j++){
        if(i % j == 0){
            pierwsza = false;
            break;
        }
    }
    if(pierwsza){
        ilosc++;
    }
}
console.log(ilosc);

//czemu przegladarka rzuca blad przy var, a nodejs nie?