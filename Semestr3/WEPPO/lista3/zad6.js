function fib() {
    var last = 1;
    var before_last = 0;

    return {
        next: function () {
            var next = last + before_last;
            before_last = last;
            last = next;
            return{
                value: next,
                done: false
            };
        }
    };
}

function* fib_gen(){
    var val_1 = 0;
    var val_2 = 1;
    while(true){
        var new_val1 = val_1 + val_2;
        val_2 = val_1;
        val_1 = new_val1;
        yield val_1;
    }
}

var it = fib();
for (var i; i = it.next(), !it.done;){
    if (i.value > 55)
        break;
    console.log( i.value );
}


var it = fib_gen();
for (var i; i = it.next(), !it.done;){
    if (i.value > 55)
        break;
    console.log( i.value );
}

/*for(const i of fib()){
    if(i>55){
        break;
    }
    console.log(i);
}*/



for(const i of fib_gen()){
    if(i>55){
        break;
    }
    console.log(i);
}


