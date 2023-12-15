var fs = require('fs');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);
async function czytajPlik(){
    const data = await readFileAsync('wejscie.txt', 'utf8');
    return data;
}

czytajPlik().then(zawartosc => console.log(zawartosc));
