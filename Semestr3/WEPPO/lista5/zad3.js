const { randomInt } = require('crypto');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

var losowa_liczba = randomInt(1, 100);

function promptUser() {
    return new Promise((resolve, reject) => {
        rl.question('Podaj liczbę: ', (userInput) => {
            const userNumber = parseInt(userInput);
            resolve(userNumber);
        });
    });
}

async function gra(zgadywana_liczba) {
    const answer = await promptUser();
    if (answer < zgadywana_liczba) {
        console.log("moja liczba jest wieksza");
    }
    else if (answer > zgadywana_liczba) {
        console.log("moja liczba jest mniejsza");
    }
    else {
        console.log("to jest wlasnie ta liczba");
        rl.close();
        return;
    }
    gra(zgadywana_liczba);
}
gra(losowa_liczba);