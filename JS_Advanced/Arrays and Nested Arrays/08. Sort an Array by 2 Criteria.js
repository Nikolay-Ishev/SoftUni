function sort_by_two_cr(arr) {
    const result = arr.sort((a, b) => {
        if (a.length < b.length) {
            return -1
        } else if (a.length == b.length) {
            return a.localeCompare(b);
        } else return 1
    })
    return result.join("\n")
}

console.log(sort_by_two_cr(['Isacc', 
'Theodor', 
'Jack', 
'Harrison', 
'George']))