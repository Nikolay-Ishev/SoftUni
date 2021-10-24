function rotate_el(arr, n) {
    let rotations
    if (n>arr.length) {
        rotations = n % arr.length
    } else {rotations = n}    
    while (rotations>0) {
        let last = arr.pop()
        arr.unshift(last)
        rotations--
    }
    return arr.join(" ")
}

console.log(rotate_el(['Banana', 
'Orange', 
'Coconut', 
'Apple'], 
15))
