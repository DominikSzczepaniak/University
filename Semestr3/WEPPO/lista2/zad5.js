const myObject = {};

myObject.myField = "Hello";

myObject.myMethod = function() {
  console.log(this.myField);
};

Object.defineProperty(myObject, "myProperty", {
  get: function() {
    return this.myField;
  },
  set: function(value) {
    this.myField = value;
  }
});

console.log(myObject.myField); 
myObject.myMethod(); 
myObject.myProperty = "World";
console.log(myObject.myProperty); 

const object2 = {
    _myField: 'hi',
    myMethod: function(){
        return this._myField;
    },
    get myProperty(){
        return this._myField;
    },
    set myProperty(value){
        this._myField = value
    }
}
console.log(object2.myProperty)
console.log(object2.myMethod())
object2.myProperty = 5
console.log(object2.myProperty)


//settery i gettery musza
//reszta moze