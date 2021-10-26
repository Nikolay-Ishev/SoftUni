function calorieObject(arr) {
    const result = {}
    for (let i=0;i<arr.length;i+=2) {
        foodName = arr[i]
        foodCal = arr[i+1]
        result[foodName] = Number(foodCal)
    }
    return result
}

console.log(calorieObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']))