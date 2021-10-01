function first_last(arr_1) {
    let first = Number(arr_1.shift());
    let last = Number(arr_1.pop());
    return first + last
}

console.log(first_last(['20', '30', '40']))