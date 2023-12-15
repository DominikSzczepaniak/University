var fs = require('fs');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);

async function czytajPlik(){
    const data = await readFileAsync('plikserwera.txt', 'utf8');
    return data.split('\n');
}

async function najwiecejZapytan(ile){
    const logi = await czytajPlik();
    for(var i in logi){
        logi[i] = logi[i].split(' ');
    }
    var dict = {};
    for(var i in logi){
        if(dict[logi[i][1]] == undefined){
            dict[logi[i][1]] = 1;
        }
        else{
            dict[logi[i][1]] += 1;
        }
    }
    const wyniki = [];
    for(var i in dict){
        wyniki.push([i, dict[i]]);
    }
    wyniki.sort(function(a, b){
        return b[1] - a[1];
    });
    console.log(wyniki.map(x => x[0]).slice(0, ile));
}
najwiecejZapytan(3);