function fib2(n: number): number {
    if (n <= 1) {
        return n;
    } else {
        return fib2(n - 1) + fib2(n - 2);
    }
}

function memoize2(fn : (n: number) => number) : (n: number) => number{
    var cache: {[key: number] : number} = {[0]: 0, [1]: 1};
    function mem(n: number) : number {
        if (n in cache) {
            return cache[n];
        } else {
            // var result_h = memoize2(fn);
            var result = mem(n-1) + mem(n-2);
            cache[n] = result;
            return result;
        }
    };
    return mem;
}
const test = memoize2(fib2);
console.log(test(80));

