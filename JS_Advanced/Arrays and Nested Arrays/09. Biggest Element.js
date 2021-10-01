function biggest_el(matrix) {
    return Math.max(...[].concat(...matrix));
}

console.log(biggest_el([[20, 50, 10],
[8, 33, 145]]))