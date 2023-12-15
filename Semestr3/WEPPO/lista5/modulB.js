const modulA = require('./modulA');

const funkcjaB = () => {
  console.log('Wywołano funkcję z modułu B');
  modulA.funkcjaA();
};

module.exports.funkcjaB = funkcjaB;
funkcjaB();