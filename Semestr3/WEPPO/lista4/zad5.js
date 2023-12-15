function Foo() {
    var privateVar = 123;
    function Qux() {
        console.log(privateVar);
    }
    this.Bar = function () {
        Qux();
    };
}

// Utworzenie instancji Foo
var obj = new Foo();
obj.Bar(); 
// obj.Qux(); //daje blad 
console.log(obj.privateVar)
