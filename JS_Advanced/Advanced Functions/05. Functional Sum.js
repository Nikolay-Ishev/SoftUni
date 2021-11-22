function add(num) {
    let sum = num
    function sumIt(num2) {
        sum += num2
        return sumIt
    }
    sumIt.toString = () => {return sum}

    return sumIt
}

console.log(add(1)(6)(-3).toString())