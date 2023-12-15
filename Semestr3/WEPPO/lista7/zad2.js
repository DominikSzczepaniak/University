const https = require('https');
const fs = require('fs');

const options = {
  pfx: fs.readFileSync('cert.pfx'),
  passphrase: 'test', 
};

const server = https.createServer(options, (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('asdasdasd\n');
});

const PORT = 443;

server.listen(PORT, () => {
  console.log(`Server running at https://localhost:${PORT}/`);
});
