function autoCompany(strArr) {
    const carBrands = {}
    for (carStr of strArr) {
        [brand, model, number] = carStr.split(` | `)
        if (!carBrands[brand]) {
            carBrands[brand] = {}
            carBrands[brand][model] = Number(number)
        }
        else if(!carBrands[brand][model]) {
            carBrands[brand][model] = Number(number)
        }
        else {carBrands[brand][model] += Number(number)}
    }
    for (const [key, value] of Object.entries(carBrands)) {
        console.log(key);
        for (const [k, v] of Object.entries(value)) {
            console.log(`###${k} -> ${v}`);
          }
      }
}

autoCompany(['Audi | Q7 | 1000',
'Audi | Q6 | 100',
'BMW | X5 | 1000',
'BMW | X6 | 100',
'Citroen | C4 | 123',
'Volga | GAZ-24 | 1000000',
'Lada | Niva | 1000000',
'Lada | Jigula | 1000000',
'Citroen | C4 | 22',
'Citroen | C5 | 10'])