function n_sum(n, m) {
    let num_1 = Number(n);
    let num_2 = Number(m)

    let result = 0
 
    for (let i = num_1; i<= num_2; i++) {
        result += i
    }
    return result;
}

console.log(n_sum("1", "5"))