function fib(n) {
    if (n <= 1) {
        return n;
    } else {
        return memoizedFib(n);
    }
}

function memoize(fn) {
    var cache = {};
    return function (n) {
        if (n in cache) {
            return cache[n];
        } else {
            var result = fn(n);
            cache[n] = result;
            return result;
        }
    };
}

function fib2(n) {
    if (n <= 1) {
        return n;
    } else {
        return fib2(n - 1) + fib2(n - 2);
    }
}

fib2 = memoize(fib2)

console.log(fib2(50)); // Przykład użycia
