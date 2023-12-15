const express = require('express');
const session = require('express-session');
const FileStore = require('session-file-store')(session);

const app = express();
const port = 3000;

app.use(
  session({
    store: new FileStore(), 
    secret: 'mySecretKey',  
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }, 
  })
);

app.get('/add-to-session', (req, res) => {
  req.session.exampleValue = 'Hello, this is a session value!';
  res.send('Wartość dodana do sesji!');
});

app.get('/get-from-session', (req, res) => {
  const exampleValue = req.session.exampleValue || 'Brak wartości w sesji.';
  res.send(`Wartość z sesji: ${exampleValue}`);
});

app.get('/clear-session', (req, res) => {
  delete req.session.exampleValue;
  res.send('Wartość usunięta z sesji!');
});

app.listen(port, () => {
  console.log(`Aplikacja działa na http://localhost:${port}`);
});
