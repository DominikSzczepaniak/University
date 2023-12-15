const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const app = express();
const port = 3000;


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

const dataStorage = new Map();
app.get('/', (req, res) => {
    const error = req.cookies.error || null;
    res.clearCookie('error');
    res.render('form', { error });
});
app.post('/', (req, res) => {
    const { firstName, lastName, course, tasks } = req.body;
    if (!firstName || !lastName || !course) {
        res.cookie('error', 'Wypełnij wszystkie pola!', { httpOnly: true });
        return res.redirect('/');
    }

    const key = Date.now().toString();
    dataStorage.set(key, { firstName, lastName, course, tasks });
    res.cookie('dataKey', key, { httpOnly: true });
    res.redirect('/print');
});
app.get('/print', (req, res) => {
    const dataKey = req.cookies.dataKey;
    const data = dataStorage.get(dataKey);
    if (!dataKey || !data) {
        return res.redirect('/');
    }
    res.render('print', { ...data });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
