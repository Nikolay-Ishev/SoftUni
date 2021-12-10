class Restaurant {
    constructor (budget) {
        this.budgetMoney = budget
        this.menu = {}
        this.stockProducts = {}
        this.history = []
    }

    loadProducts(productsArr) {
        for (let p of productsArr) {
            let [pName, pQuantity, totalPrice] = p.split(' ')
            pQuantity = Number(pQuantity)
            totalPrice = Number(totalPrice)
            if (totalPrice <= this.budgetMoney) {
                if (!this.stockProducts[pName]) {
                    this.stockProducts[pName] = 0
                }
                this.stockProducts[pName] += pQuantity
                this.budgetMoney -= totalPrice
                this.history.push(`Successfully loaded ${pQuantity} ${pName}`)
            }
            else {this.history.push(`There was not enough money to load ${pQuantity} ${pName}`)}
        }
        return this.history.join('\n')
    }

    addToMenu(meal, pNeededArr, pPrice) {
        if (this.menu[meal]) {
            return `The ${meal} is already in the our menu, try something different.`
        }
        let productsObj = {}
        for (let p of pNeededArr) {
            let [pName, pQuantity] = p.split(' ')
            productsObj[pName] = Number(pQuantity)
        }
        this.menu[meal] = {
            products: productsObj,
            price: Number(pPrice)
        }
        const size = Object.keys(this.menu).length
        if (size > 1) {
            return `Great idea! Now with the ${meal} we have ${size} meals in the menu, other ideas?`
        }
        else {return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`}
    }

    showTheMenu() {
        const size = Object.keys(this.menu).length
        if (size == 0) {
            return "Our menu is not ready yet, please come later..."
        }
        else {
            let result = []
            for (const [key, value] of Object.entries(this.menu)) {
                result.push(`${key} - $ ${value.price}`);
            }
            return result.join(`\n`)
        }
    }

    makeTheOrder(meal) {
        //check if meal exist in menu
        if (!this.menu[meal]) {
            return `There is not ${meal} yet in our menu, do you want to order something else?`
        }
        //check if all the products are in stock
        for (let [key, value] of Object.entries(this.menu[meal].products)) {
            if (!this.stockProducts[key] || this.stockProducts[key] < value) {
                return `For the time being, we cannot complete your order (${meal}), we are very sorry...`
            }
        }
        //prepare meal 
        for (const [key, value] of Object.entries(this.menu[meal].products)) {
            this.stockProducts[key] -= value;
        }
        this.budgetMoney += this.menu[meal].price
        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${this.menu[meal].price}.`

    }
}


let test = new Restaurant(1000);
test.loadProducts(['Yogurt 30 3', 'Honey 50 4', 'Strawberries 20 10', 'Banana 5 1']);
test.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99);
console.log(test.makeTheOrder('frozenYogurt'))
console.log(test.makeTheOrder('frozenYogurt'))
console.log(test.makeTheOrder('frozenYogurt'))
console.log(test.makeTheOrder('frozenYogurt'))
console.log(test.makeTheOrder('frozenYogurt'))