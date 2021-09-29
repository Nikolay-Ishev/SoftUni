function number_modificator(str_number, el_1, el_2, el_3, el_4, el_5) {
    let number = Number(str_number)
    el_list = [el_1, el_2, el_3, el_4, el_5]
    for (let i=0; i<5; i++) {
        switch (el_list[i]) {
            case 'chop':
                number /= 2;
                console.log(number)
                break;
            case 'dice':
                number = Math.sqrt(number);
                console.log(number)
                break;
            case 'spice':
                number += 1
                console.log(number)
                break;
            case 'bake':
                number *= 3
                console.log(number)
                break;
            case 'fillet':
                number -= 0.2 * number
                console.log(number)
        }
    }
}

number_modificator('32', 'chop', 'chop', 'chop', 'chop', 'chop')