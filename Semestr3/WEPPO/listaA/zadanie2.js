const { Client } = require('pg');
const client = new Client({
    user: 'projekt',
    host: 'localhost',
    database: 'listaaweppo1',
    password: 'projekt',
    port: 5432
});

async function prepare() {
    const query = 'DROP TABLE IF EXISTS OSOBA';
    await client.query(query);
    const query2 = 'CREATE TABLE OSOBA(id SERIAL PRIMARY KEY, imie VARCHAR(255), nazwisko VARCHAR(255), plec VARCHAR(1))';
    await client.query(query2);
    const query3 = 'DROP TABLE IF EXISTS MIEJSCE_PRACY';
    await client.query(query3);
}

client.connect();
async function run() {
    async function insertPerson(imie, nazwisko, plec) {
        const query = 'INSERT INTO OSOBA(imie, nazwisko, plec) VALUES($1, $2, $3) RETURNING id';
        const values = [imie, nazwisko, plec];
        const result = await client.query(query, values);
        const insertedId = result.rows[0].id;
        return insertedId;
    }
    var id = await insertPerson("Jan", "Kowalski", "M");

    async function updatePerson(id, newImie, newNazwisko) {
        const query = 'UPDATE OSOBA SET imie = $1, nazwisko = $2 WHERE id = $3';
        const values = [newImie, newNazwisko, id];
        await client.query(query, values);
    }

    await updatePerson(id, 'NowaKowalska');
    async function deletePerson(id) {
        const query = 'DELETE FROM OSOBA WHERE id = $1';
        const values = [id];
        await client.query(query, values);
    }
    await deletePerson(1);

    return;
}
prepare().then(() => {
    run().then(() => {
        client.end();
    });
});
