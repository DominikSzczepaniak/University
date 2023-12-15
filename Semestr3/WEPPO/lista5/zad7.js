const fs = require('fs');

// klasyczny interfejs programowania asynchronicznego z użyciem funkcji zwrotnej (callback)
function readAFileClassic(filePath, callback) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            callback(err, null);
        } else {
            callback(null, data);
        }
    });
}

// funkcja przyjmująca argumenty jak fs.readFile, ale zwracająca Promise
function readAFileWithPromise(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}

const util = require('util');
const readFilePromise = util.promisify(fs.readFile);

// funkcja używająca util.promisify
async function readAFileWithUtilPromisify(filePath) {
    try {
        return await readFilePromise(filePath, 'utf8');
    } catch (error) {
        throw error;
    }
}

// funkcja z użyciem fs.promises
async function readAFileWithFsPromises(filePath) {
    try {
        return await fs.promises.readFile(filePath, 'utf8');
    } catch (error) {
        throw error;
    }
}

readAFileWithPromise(sciezkaPlik)
    .then(data => {
        console.log('Pomyślnie odczytano plik:', data);
    })
    .catch(error => {
        console.error('Błąd podczas odczytu pliku:', error);
    });

async function readFileAsync(filePath) {
    try {
        const data = await readAFileWithFsPromises(filePath);
        console.log('Pomyślnie odczytano plik:', data);
    } catch (error) {
        console.error('Błąd podczas odczytu pliku:', error);
    }
}

readFileAsync();

