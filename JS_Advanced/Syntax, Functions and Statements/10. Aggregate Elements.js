function aggregate_el(params) {
    arrSum = function(arr){
        return arr.reduce(function(a,b){
          return a + b
        }, 0);
      }
    console.log(arrSum(params))

    inverse_sum = 0
    for (let i = 0; i < params.length; i++) {
        inverse_sum += 1 / params[i]
    }
    console.log(inverse_sum)
    console.log(params.join(''))
}

aggregate_el([1, 2, 3])
aggregate_el([2, 3, 5])