function solution() {
    const recipes = {
        "apple": {"protein": 0, "carbohydrate": 1, "fat": 0, "flavour": 2},
        "lemonade": {"protein": 0, "carbohydrate": 10, "fat": 0, "flavour": 20},
        "burger": {"protein": 0, "carbohydrate": 5, "fat": 7, "flavour": 3},
        "eggs": {"protein": 5, "carbohydrate": 0, "fat": 1, "flavour": 1},
        "turkey": {"protein": 10, "carbohydrate": 10, "fat": 10, "flavour": 10},
    }

    const storedEl = {
        "protein":0, "carbohydrate": 0, "fat": 0, "flavour": 0
    }

    function result(str) {
        const command = str.split(` `)
        if (command[0] == `restock`) {
            let el = command[1]
            let quantity = Number(command[2])
            storedEl[el] += quantity
            return 'Success'
        } else if (command[0] == `prepare`) {
            let recipe = command[1]
            let quantity = Number(command[2])
            for (el in recipes[recipe]) {
                if (recipes[recipe][el] * quantity > storedEl[el]) {
                    return `Error: not enough ${el} in stock`
                } else {storedEl[el] -= recipes[recipe][el] * quantity}
            }
            return 'Success'
        } else {
            return `protein=${storedEl["protein"]} carbohydrate=${storedEl["carbohydrate"]} fat=${storedEl["fat"]} flavour=${storedEl["flavour"]}`
        }
    }
    return result
}

let manager = solution(); 
console.log (manager("restock flavour 50")); 
console.log (manager("prepare lemonade 4"));
console.log (manager("restock carbohydrate 10"));
console.log (manager("prepare apple 1"));
console.log (manager("restock fat 10"));
console.log (manager("prepare burger 1"));
console.log (manager("report"));





