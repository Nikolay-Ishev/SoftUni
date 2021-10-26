function carFactory(request) {
    let result = {}
    result.model = request.model

    if (request.power <= 90) {
        result.engine = { power: 90,
            volume: 1800 }
    } else if (request.power <= 120) {
        result.engine = { power: 120,
            volume: 2400 }
    } else {result.engine = { power: 200, volume: 3500 }}

    result.carriage = {type: request.carriage, color: request.color}

    if (request.wheelsize % 2 == 0) {request.wheelsize -= 1};
    result.wheels = [request.wheelsize, request.wheelsize, request.wheelsize, request.wheelsize]

    //create new array with length 4, filled with r.w from i0 to i4
    // result.wheels = new Array(4).fill(request.wheelsize, 0, 4)

    return result
}

console.log(carFactory({ model: 'Opel Vectra',
power: 110,
color: 'grey',
carriage: 'coupe',
wheelsize: 17 }))