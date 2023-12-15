const express = require('express');
const crypto = require('crypto');

const app = express();
const port = 3000;


app.get('/secured-endpoint', (req, res) => {
  const originalData = 'Hello, this is secure data!';

  const encryptedData = crypto.createCipher('aes-256-ctr', 'secret-key').update(originalData, 'utf-8', 'hex');

  const signature = crypto.createHmac('sha256', 'signature-key').update(originalData).digest('hex');

  const queryString = `?data=${encryptedData}&signature=${signature}`;
  res.send(`Zabezpieczone dane: ${originalData}<br>URL: /secured-endpoint${queryString}`);
});
app.get('/read-secured-endpoint', (req, res) => {
  const { data, signature } = req.query;

  const isValidSignature = crypto.createHmac('sha256', 'signature-key').update(data).digest('hex') === signature;

  if (isValidSignature) {

    const decryptedData = crypto.createDecipher('aes-256-ctr', 'secret-key').update(data, 'hex', 'utf-8');
    res.send(`Odczytane dane: ${decryptedData}`);
  } else {
    res.status(400).send('Błąd weryfikacji podpisu.');
  }
});

app.listen(port, () => {
  console.log(`Aplikacja działa na http://localhost:${port}`);
});
