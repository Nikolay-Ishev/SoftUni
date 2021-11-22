function arguments(...args) {
    let obj = {}
    for (let arg of args) {
        const type = typeof arg
        console.log(`${type}: ${arg}`)
        if (!obj.hasOwnProperty(type)) {
            obj[type] = 0
        }
        obj[type] += 1
    }

    let sortable = [];
    for (let el in obj) {
        sortable.push([el, obj[el]]);
    }

    sortable.sort((a, b) => (b[1] - a[1]))
    for (let el of sortable) {
        console.log(`${el[0]} = ${el[1]}`)
    }
}

arguments({ name: 'bob'}, 3.333, 9.999)