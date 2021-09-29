function solve(num1, num2, operator_1){
    str_conv = "num1 " + operator_1 + " num2"
    console.log(eval(str_conv))
}

solve(5, 6, '+')

function solve_2(num1, num2, operator_1){
    let result;
    switch (operator_1) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '/': result = num1 / num2; break;
        case '*': result = num1 * num2; break;
        case '%': result = num1 % num2; break;
        case '**': result = num1 ** num2; break;
    }
    console.log(result)
}

solve_2(5, 5, '**')