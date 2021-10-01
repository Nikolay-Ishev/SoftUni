function smallest_two(arr_1) {
    numArray = arr_1.sort((a, b) => a - b);
    return `${numArray[0]} ${numArray[1]}`
}

console.log(smallest_two([3, 0, 10, 4, 7, 3]))