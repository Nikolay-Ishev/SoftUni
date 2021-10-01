function n_sequence(length_s, sum_el) {
    let result_list = [1]
    for (let i = 1; i < length_s; i++) {
        let last_el
        if (i - sum_el <= 0) {
            last_el = result_list.slice(0, sum_el)
        } else {
            last_el = result_list.slice(i - sum_el, i)
        }

        let next_el = last_el.reduce((a, b) => a + b, 0)
        result_list.push(next_el)
    }
    return result_list
}

console.log(n_sequence(8, 2))