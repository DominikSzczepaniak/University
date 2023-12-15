const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;

app.use(cookieParser());

app.get('/set-cookie', (req, res) => {
    res.cookie('exampleCookie', 'Hello, this is a cookie!');
    res.send('Ciasteczko ustawione!');
});

app.get('/get-cookie', (req, res) => {
    const exampleCookie = req.cookies.exampleCookie;
    res.send(`Wartość ciasteczka: ${exampleCookie}`);
});

app.get('/clear-cookie', (req, res) => {
    res.clearCookie('exampleCookie');
    res.send('Ciasteczko usunięte!');
});


app.listen(port, () => {
    console.log(`Aplikacja działa na http://localhost:${port}`);
});

// nie mozna sie dowiedziec czy ktos ma cookies czy nie w przegladarce
//mozna zalozyc ze jesli odpali strone expressjs to powininen miec cookies