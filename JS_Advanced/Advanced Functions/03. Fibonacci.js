function getFibonator() {
    let first = 0
    let second = 1
    function result() {
        let next = first + second
        first = second
        second = next
        return first
    }
    return result
}

//Fibonacci Series using Recursion
let n = 9;
     
// function returns the Fibonacci number
function fib(n) {
if (n <= 1)
    return n;
return fib(n-1) + fib(n-2);
}



console.log(fib(5))