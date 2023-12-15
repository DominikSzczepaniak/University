const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.get('/download', (req, res) => {
    const dynamicData = 'To są dynamicznie utworzone dane na serwerze.';
    const tempDir = path.join(__dirname, 'temp');
    if (!fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir);
    }
    const filePath = path.join(tempDir, 'dynamic_file.txt');
    fs.writeFileSync(filePath, dynamicData);
    res.setHeader('Content-Disposition', 'attachment; filename=dynamic_file.txt');
    res.setHeader('Content-Type', 'text/plain');
    const stream = fs.createReadStream(filePath);
    stream.pipe(res);
});

app.listen(port, () => {
    console.log(`Aplikacja działa na http://localhost:${port}`);
});
