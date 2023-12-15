const modulB = require('./modulB');

const funkcjaA = () => {
  console.log('Wywołano funkcję z modułu A');
  modulB.funkcjaB();
};

module.exports.funkcjaA = funkcjaA;
