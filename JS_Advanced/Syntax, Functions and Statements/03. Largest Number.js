function largest(a, b, c) {
    if (a > b) {
        if (a > c) {
            result = a;
        }
        else {
            result = c
        }
    } else if (b > c) {
        result = b
    }else result =c
    console.log(`The largest number is ${result}.`)
}

function secondSolution(...params) { 
    console.log(`The largest number is ${Math.max(...params)}.`);
}

largest(1 ,2 ,3)
largest(3, 2 ,1)
largest(5,2,7)