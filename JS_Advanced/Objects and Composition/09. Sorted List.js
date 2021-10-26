function createSortedList() {
    let a = {
        collection: [],

        size : 0,

        wrong_i(i) {
            if (i<0 || i>=this.collection.length) {
                return true
            } else {return false}
        },

        add(el) {
            if (isNaN(el)) {return}
            this.collection.push(el)
            this.collection = this.collection.sort((a, b) => a - b)
            this.size ++
        },

        remove(i) {
            if (isNaN(i) || this.wrong_i(i)) {return};
            this.collection.splice(i, 1)
            this.size--
        },

        get(i) {
            if (isNaN(i) || this.wrong_i(i)) {return};
            return this.collection[i]
        }, 
    }
    return a
}



let list = createSortedList();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1)); 
list.remove(1);
console.log(list.get(1));
console.log(list.size)