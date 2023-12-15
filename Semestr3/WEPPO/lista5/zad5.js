const https = require('https');

function fetchWebsiteContent(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      let data = '';

      response.on('data', (chunk) => {
        data += chunk;
      });

      response.on('end', () => {
        resolve(data);
      });

      response.on('error', (error) => {
        reject(error);
      });
    });
  });
}

// Przykładowe użycie:
const websiteURL = 'https://www.example.com'; // Tutaj podaj adres strony, którą chcesz pobrać
fetchWebsiteContent(websiteURL)
  .then((data) => {
    console.log('Zawartość strony:');
    console.log(data);
  })
  .catch((error) => {
    console.error('Wystąpił błąd podczas pobierania zawartości strony:', error);
  });
