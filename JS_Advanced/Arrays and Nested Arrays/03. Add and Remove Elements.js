function add_remove_n(arr) {
    let result_arr = []
    for (let i = 0; i < arr.length; i++) {
        let command = arr[i]
        let number = i + 1
        if (command == "add") {
            result_arr.push(number)
        }

        else if (command == "remove") {
            result_arr.pop()
        }
    }
    if (result_arr.length == 0) {
        console.log("Empty")
    }
    else {        
        console.log(result_arr.join(`\n`))
        
    }
}


add_remove_n(['add',
    'add',
    'remove',
    'add',
    'add'])