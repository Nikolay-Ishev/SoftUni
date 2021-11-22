function cars(arr) {
    const objects = []

    function car(name) {
        let that = {}; // Create an empty object
        that.name = name; // Add it a "name" property
        return that; // Return the object
      };

    for (el of arr) {
        command = el.split(` `)
        if (command[0] == `create`) {
            if (command.length == 2) {
                objects.push(car(command[1]))
            }
            else if (command.length == 4) {
                newObj
                objects.push
            }
        }
    }
}