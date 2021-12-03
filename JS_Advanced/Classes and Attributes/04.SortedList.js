class List {
    constructor() {
        this._numbers = []
        this.size = 0
    }
    
    checkIndex(index) {
        if (index < 0 || index >= this._numbers.length) {
            throw new Error(`invalid index`)
        }
    }

    add(element) {
        this._numbers.push(element)
        this._numbers.sort((a, b) => a - b)
        this.size += 1
    }

    get(index) {
        this.checkIndex(index)
        return this._numbers[index]
    }

    remove(index) {
        this.checkIndex(index)
        this._numbers.splice(index, 1)
        this.size -= 1
    }
}


let list = new List();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1)); 
list.remove(1);
console.log(list)
console.log(list.get(1));
console.log(list.get(12))