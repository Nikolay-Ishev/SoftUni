class VegetableStore {
    constructor(owner, location) {
        this.owner = owner
        this.location = location
        this.availableProducts = []
    }

    loadingVegetables (vegetablesArr) {
        //Example: ["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2"…]

        let result = []

        for (let el of vegetablesArr) {
            let alreadyPresent = false
            let [pType, pQuantity, pPrice] = el.split(" ")

            pQuantity = Number(pQuantity)
            pPrice = Number(pPrice)

            if (!result.includes(pType)) {
                result.push(pType)
            }

            for (let pr of this.availableProducts) {
                if (pr.type == pType) {
                    //add the new pQuantity to the old one 
                    alreadyPresent = true
                    pr.quantity += pQuantity
                    //update the old pPrice per kilogram only if the current one is higher
                    if (pPrice > pr.price) {
                        pr.price = pPrice
                    }
                }
            }

            //Otherwise, should add the vegetable, with properties: {type, quantity, price} to the availableProducts array
            if (alreadyPresent == false) {
                this.availableProducts.push({type: pType, quantity: pQuantity, price: pPrice})
            }
        }
        //finally return a string in the following format: `Successfully added {type1}, {type2}, …{typeN}` with UNIQUE el
        let resultStr = result.join(", ")
        return `Successfully added ${resultStr}`
    }

    buyingVegetables (selectedProductsArr) {
        let totalPrice = 0
        for (let el of selectedProductsArr) {
            let [prType, prQuantity] = el.split(" ")
            prQuantity = Number(prQuantity)
            let alreadyPresent = false
            for (let pr of this.availableProducts) {
                if (pr.type == prType) {
                    alreadyPresent = true
                    //If the quantity selected by the customer for a given vegetable is greater than the quantity recorded in availableProducts
                    if (prQuantity > pr.quantity) {
                        throw Error(`The quantity ${prQuantity} for the vegetable ${pr.type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
                    }
                    // otherwise reduce the quantity recorded in the availableProducts array and update the total price.
                    else {
                        let currentPrice = pr.price * prQuantity
                        pr.quantity -= prQuantity
                        totalPrice += currentPrice
                        break
                    }
                }
            }

            //If the type of the current vegetable is not present in availableProducts
            if (alreadyPresent == false) {
                throw Error(`${prType} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
            }
        }
        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`
    }

    rottingVegetable (prType, prQuantity) {
        let alreadyPresent = false
        for (let pr of this.availableProducts) {
            if (pr.type == prType) {
                alreadyPresent = true

                //If the submitted quantity is greater than the quantity recorded in the availableProducts 
                if (prQuantity > pr.quantity) {
                    pr.quantity = 0
                    return `The entire quantity of the ${prType} has been removed.`
                }

                //Otherwise, reduce the quantity recorded in the array availableProducts and return a str
                else {
                    pr.quantity -= prQuantity
                    return `Some quantity of the ${prType} has been removed.`
                }
            }
        }

        //If the submitted type is not present in the availableProducts array, throws an error
        if (alreadyPresent == false) {
            throw Error(`${prType} is not available in the store.`)
        }
    }

    revision () {
        this.availableProducts.sort((a, b) => a.price - b.price)
        let result = []
        result.push("Available vegetables:")

        for (let pr of this.availableProducts) {
            result.push(`${pr.type}-${pr.quantity}-$${pr.price}`)
        }

        result.push(`The owner of the store is ${this.owner}, and the location is ${this.location}.`)
        return result.join("\n")
    }
}

let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
console.log(vegStore.rottingVegetable("Okra", 1));
console.log(vegStore.rottingVegetable("Okra", 2.5));
console.log(vegStore.buyingVegetables(["Beans 8", "Celery 1.5"]));
console.log(vegStore.revision());
