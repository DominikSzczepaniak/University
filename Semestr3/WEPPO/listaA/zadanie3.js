const { Client } = require('pg');
const client = new Client({
    user: 'projekt',
    host: 'localhost',
    database: 'listaaweppo1',
    password: 'projekt',
    port: 5432
});
client.connect();

async function prepare() {
    const query = 'DROP TABLE IF EXISTS OSOBA';
    await client.query(query);
    const query2 = 'DROP TABLE IF EXISTS MIEJSCE_PRACY';
    await client.query(query2);
    const query3 = 'CREATE TABLE MIEJSCE_PRACY(id SERIAL PRIMARY KEY, nazwa VARCHAR(100), lokalizacja VARCHAR(255))';
    await client.query(query3);
    const query4 = 'CREATE TABLE OSOBA(id SERIAL PRIMARY KEY, imie VARCHAR(255), nazwisko VARCHAR(255), plec VARCHAR(1), miejsce_pracy_id INTEGER REFERENCES MIEJSCE_PRACY(id))';
    await client.query(query4);
}

async function run() {
    async function dodajNoweMiejscePracyIOsobe(nazwaMiejsca, lokalizacja, imie, nazwisko, plec) {
        const miejscePracyQuery = 'INSERT INTO MIEJSCE_PRACY (nazwa, lokalizacja) VALUES ($1, $2) RETURNING id';
        const miejscePracyValues = [nazwaMiejsca, lokalizacja];
        const miejscePracyResult = await client.query(miejscePracyQuery, miejscePracyValues);
        const idNowegoMiejscaPracy = miejscePracyResult.rows[0].id;

        const osobaQuery = 'INSERT INTO OSOBA (imie, nazwisko, miejsce_pracy_id, plec) VALUES ($1, $2, $3, $4)';
        const osobaValues = [imie, nazwisko, idNowegoMiejscaPracy, plec];
        await client.query(osobaQuery, osobaValues);
        await client.query('COMMIT');
    }
    await dodajNoweMiejscePracyIOsobe('AGH', 'Kraków', 'Jan', 'Kowalski', 'M');

}

prepare().then(() => {
    run().then(() => {
        client.end();
    });
});

