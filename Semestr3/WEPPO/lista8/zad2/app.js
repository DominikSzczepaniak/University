const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(express.static('public')); 
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  res.render('index', { title: 'Strona główna' });
});

app.get('/select', (req, res) => {
  const options = ['Opcja 1', 'Opcja 2', 'Opcja 3'];
  res.render('select', { title: 'Lista rozwijalna', options });
});

app.listen(port, () => {
  console.log(`Aplikacja działa na http://localhost:${port}`);
});
