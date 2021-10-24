function increasing_arr(arr) {
    let result_arr = []
    if (arr.length == 0) {
        return result_arr
    }
    result_arr.push(arr[0])
    for (let i=1;i<arr.length;i++) {
        let last_i = result_arr.length - 1
        if (arr[i] >= result_arr[last_i]) {
            result_arr.push(arr[i])
        }
    }
    return result_arr
}

function increasing_arr2(arr) {
    biggest = Number.MIN_SAFE_INTEGER
    return arr.filter(el => {
        if (el >= biggest) {
            biggest = el;
            return true
        }        
    })
}

console.log(increasing_arr([]))