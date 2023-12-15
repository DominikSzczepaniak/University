function createGenerator(limit) {
    return function () {
        var _state = 0;
        return {
            next: function () {
                return {
                    value: _state,
                    done: _state++ >= limit
                }
            }
        }
    }
}

var foo2 = {
    [Symbol.iterator]: createGenerator(5)
};
for (var f of foo2)
    console.log(f)

var foo = {
    [Symbol.iterator]: createGenerator(15)
};

for (var f of foo){
    console.log(f);
}