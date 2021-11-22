function list_processor(arr) {
    let resultArr = []
    for (el of arr) {
        if (el === 'print') {
            console.log(resultArr.join(`,`))
            continue
        }
        [action, str] = el.split(` `)
        if (action == `add`) {
            resultArr.push(str)
        } else if (action == `remove`) {
            resultArr = resultArr.filter(i => i !== str)
        }
    }
}

list_processor(['add hello', 'add again', 'remove hello', 'add again', 'print'])