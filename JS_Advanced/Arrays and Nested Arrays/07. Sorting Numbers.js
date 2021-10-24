function min_max_sort_arr(arr) {   
    arr.sort(function(a, b) {
        return a - b;
      });
    let result_arr = []
    const count = Math.floor(arr.length/2)
    while (arr.length > 0) {
        result_arr.push(arr.shift(), arr.pop())
    }
    return result_arr 
}

console.log(min_max_sort_arr([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))