function juiceFlavors(arr) {
    const juiceFlavors = {}
    const juiceBottles = {}
    for (let jStr of arr) {
        [jName, jQuantity] = jStr.split(` => `)
        if (!juiceFlavors[jName]) {
            juiceFlavors[jName] = 0
        }
        juiceFlavors[jName] += Number(jQuantity)
        while (juiceFlavors[jName] >= 1000) {
            if (!juiceBottles[jName]) {
                juiceBottles[jName] = 0
            }
            juiceBottles[jName] += 1
            juiceFlavors[jName] -= 1000
        }
    }
    for (const [key, value] of Object.entries(juiceBottles)) {
        console.log(`${key} => ${value}`);
      }
}

juiceFlavors(['Orange => 2000',
'Peach => 1432',
'Banana => 450',
'Peach => 600',
'Strawberry => 549'])