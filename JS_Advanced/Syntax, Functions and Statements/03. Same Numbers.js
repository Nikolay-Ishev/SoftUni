function same_nums(num) {
    same = true
    nums_sum = 0
    let num_str = String(num).split('')
    for (let i=0; i < num_str.length; i++) {
        nums_sum += Number(num_str[i]);
        if (same = true) {
            if (Number(num_str[i]) !== Number(num_str[0])) {
                same = false} 
            }               
    }
    console.log(same)
    console.log(nums_sum)
}

same_nums(222)
same_nums(1234)