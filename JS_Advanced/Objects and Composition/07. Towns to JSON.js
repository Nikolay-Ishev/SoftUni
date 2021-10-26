function jsonTowns(arr) {
    let [h1, h2, h3] = arr[0].slice(2, arr[0].length - 2).split(" | ")
    result = []
    for (let i=1;i<arr.length;i++) {
        let [town, lat, long] = arr[i].slice(2, arr[i].length - 2).split(" | ")
        let obj = {}
        obj[h1] = town
        obj[h2] = Number(parseFloat(lat).toFixed(2))
        obj[h3] = Number(parseFloat(long).toFixed(2))
        result.push(obj)
    }
    return JSON.stringify(result) 
}

console.log(jsonTowns(['| Town | Latitude | Longitude |',
'| Sofia | 42.696552 | 23.32601 |',
'| Beijing | 39.913818 | 116.363625 |']))



//console.log(result);