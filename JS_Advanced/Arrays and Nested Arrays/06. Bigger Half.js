function bigger_half(arr_n) {
    numArray = arr_n.sort((a, b) => a - b);
    const middle = Math.floor(arr_n.length / 2);
    return numArray.slice(middle)
}

console.log(bigger_half([3, 19, 14, 7, 2, 19, 6]))