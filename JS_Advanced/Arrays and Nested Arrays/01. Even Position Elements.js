function even_i(a_list) {
    let result_list = []
    for (let i = 0; i < a_list.length; i += 2) {
        result_list.push(a_list[i])
    }
    return result_list.join(" ")
}


console.log(even_i(['20', '30', '40', '50', '60']))