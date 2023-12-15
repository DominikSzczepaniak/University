const express = require('express');
const csurf = require('csurf');

const app = express();
const port = 3000;


app.use(csurf({ cookie: true }));

app.get('/form', (req, res) => {
  res.send(`
    <form action="/process" method="post">
      <input type="text" name="data" />
      <input type="hidden" name="_csrf" value="${req.csrfToken()}" />
      <button type="submit">Submit</button>
    </form>
  `);
});

app.post('/process', (req, res) => {
  const { data } = req.body;
  res.send(`Przetworzone dane: ${data}`);
});

app.listen(port, () => {
  console.log(`Aplikacja działa na http://localhost:${port}`);
});
