function storeCatalogue(arr) {
    catalogue = {}
    for (p of arr) {
        [product, price] = p.split(" : ")
        price = Number(price)
        let letter = product.toUpperCase()[0]
        if (!catalogue[letter]) {
            catalogue[letter] = {}
        }
        catalogue[letter][product] = price
    }
    const catalogueArr = Object.entries(catalogue).sort((a,b) => a[0].localeCompare(b[0]))
    for (let word of catalogueArr) {
        items = word[1]
        console.log(word[0])
        const itemsArr = Object.entries(items).sort((a,b) => a[0].localeCompare(b[0]))
        for (let item of itemsArr) {
            console.log(`  ${item[0]}: ${item[1]}`)
        }
    }
}

storeCatalogue(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10'])