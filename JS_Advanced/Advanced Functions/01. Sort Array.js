function sort(arr, command) {
    if (command == 'asc') {
        return arr.sort(function(a, b){return a-b})
    } else {return arr.sort(function(a, b){return b-a})}    
}

console.log(sort([14, 7, 17, 6, 8], 'asc'))