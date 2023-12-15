const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;

// Utwórz katalog, jeśli nie istnieje
const uploadDirectory = 'uploads/';
if (!fs.existsSync(uploadDirectory)) {
    fs.mkdirSync(uploadDirectory);
}

// Ustawienia dla Multer
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, uploadDirectory);
    },
    filename: function (req, file, cb) {
        const ext = path.extname(file.originalname);
        cb(null, file.fieldname + '-' + Date.now() + ext);
    }
});

const upload = multer({ storage: storage });

// Wyświetlanie formularza
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Obsługa przesyłania pliku
app.post('/upload', upload.single('fileInput'), (req, res) => {
    res.send('File uploaded successfully!');
});

// Start serwera
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
