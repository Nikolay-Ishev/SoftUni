function neg_pos_numbers(a_list) {
    let result_list = [];
    for (let i = 0; i < a_list.length; i++) {
        if (a_list[i] < 0) {
            result_list.unshift(a_list[i]);
        } else {
            result_list.push(a_list[i]);
        }
    }
    return result_list.join("\n");
}
console.log(neg_pos_numbers([7, -2, 8, 9]));

