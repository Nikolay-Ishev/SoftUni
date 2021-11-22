function solution(number) {
    return (a) => number + a
}

let add7 = solution(7);
console.log(add7(2));
console.log(add7(3));