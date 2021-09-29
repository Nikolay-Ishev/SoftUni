function validity_checker(x1, y1, x2, y2) {
    function v_check(n1, m1, n2, m2) {
        result_number = Math.sqrt((n1-n2)**2 + (m1-m2)**2)
        if (Number.isInteger(result_number)) {
            return "valid"}
        else return "invalid" 
    }
    console.log(`{${x1}, ${y1}} to {0, 0} is ${v_check(x1, y1, 0, 0)}`)
    console.log(`{${x2}, ${y2}} to {0, 0} is ${v_check(x2, y2, 0, 0)}`)
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${v_check(x1, y1, x2, y2)}`)
}


validity_checker(3, 0, 0, 4)
validity_checker(2, 1, 1, 1)
