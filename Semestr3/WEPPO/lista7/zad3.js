const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.get('/', (req, res) => {
  res.render('form');
});
app.get('/', (req, res) => {
    res.render('form', { error: null }); 
  });
app.post('/', (req, res) => {
    const { firstName, lastName, course, tasks } = req.body;
    let error;
    if (!firstName || !lastName || !course) {
      error = 'Wypełnij wszystkie pola!';
      return res.render('form', { error });
    }
  
    res.render('print', { firstName, lastName, course, tasks: tasks || [], error });
  });

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
