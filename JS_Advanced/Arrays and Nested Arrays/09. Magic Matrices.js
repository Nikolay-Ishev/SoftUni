function magic_matrix(arr) {
    let compare_sum = arr[0].reduce((a, b) => a + b, 0)
    for (let r_i=1; r_i<arr.length;r_i++) {
        if (arr[r_i].reduce((a, b) => a + b, 0) != compare_sum) {
            return false
        }
    }
    for (let c_i=0;c_i<arr[0].length;c_i++) {
        let c_sum = 0
        for (let r_i=0;r_i<arr.length;r_i++) {
            c_sum += arr[c_i][r_i]
        }
        if (c_sum != compare_sum) {
            return false
        } 
    }
    return true   
}


console.log(magic_matrix([[0],
    [0],
    [0]]))