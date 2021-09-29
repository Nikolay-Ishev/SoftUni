function fruit_prize(fruit, grams, price) {
    weight = (grams/1000).toFixed(2)
    money = (grams/1000 * price).toFixed(2)
    result = `I need $${money} to buy ${weight} kilograms ${fruit}.`
    console.log(result)
}

fruit_prize('orange', 2500, 1.80)