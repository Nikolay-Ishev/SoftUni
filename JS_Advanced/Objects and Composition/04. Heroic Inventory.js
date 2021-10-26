function heroicInventory(arr) {
    let result = []
    for (let hero of arr) {
        let [hName, level, items] = hero.split(" / ")
        let obj = {name: hName, level: Number(level)};
        // if (items != undefined && items != '') {
        //     obj.items = items.split(", ")
        // } else {obj.items = []}
        obj.items = items ? items.split(", ") : [];
        result.push(obj)       
    }
    return JSON.stringify(result)
}

console.log(heroicInventory(['Isacc / 25',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']))