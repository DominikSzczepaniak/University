function czyPropertyZObiektu(obiekt, propertyName){
    return obiekt.hasOwnProperty(propertyName);
}
function czyPropertyZPrototypu(obiekt, propertyName){
    var p = obiekt;
    do{
        obiekt = p;
        if(czyPropertyZObiektu(obiekt, propertyName)){
            return true;
        }
        p = Object.getPrototypeOf(obiekt);
    }while(p);
    return false;
}
function polaWObiekcie(obiekt){
    for(let property in obiekt){
        if(czyPropertyZObiektu(obiekt, property)){
            console.log(property);
        }
    }
}
function polaWObiekcieILancuchu(obiekt){
    var p = obiekt;
    const properties = new Set();
    do{
        obiekt = p;
        for(let property in obiekt){
            if(!(property in properties)){
                properties.add(property);
            }
        }
        p = Object.getPrototypeOf(obiekt);
    }while(p);
    var answer = "";
    properties.forEach(function(value){
        answer += value + " ";
    })
    console.log(answer);
}

var p = {
    a: 11
}
var c = {
    b: 12
}
var d = {
    e: 14
}
console.log(czyPropertyZObiektu(p, "a"))
Object.setPrototypeOf(c, d);
Object.setPrototypeOf(p, c);
console.log(czyPropertyZPrototypu(p, "e"))
console.log(czyPropertyZPrototypu(p, "f"))
console.log(czyPropertyZPrototypu(c, "a"))

polaWObiekcie(p);
polaWObiekcieILancuchu(p)