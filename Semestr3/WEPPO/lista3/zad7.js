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

function* take(it, top){
    var licz = 0;
    for(var i of it()){
        yield i;
        licz+=1;
        if(licz == top){
            break;
        }
    }
}
for (let num of take(fib_gen, 10)){
    console.log(num);
}



