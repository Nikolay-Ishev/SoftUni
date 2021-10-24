function return_nth_el(arr, n) {
    let result = []
    for (let i = 0; i < arr.length; i += n) {
        console.log(result)
        result.push(arr[i])
    }
    return result
}


console.log(return_nth_el(['dsa',
'asd', 
'test', 
'tset'], 
2));

