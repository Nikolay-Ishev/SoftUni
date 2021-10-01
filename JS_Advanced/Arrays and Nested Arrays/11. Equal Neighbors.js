function equal_neighbors(nested_array) {
    let neighbors = 0

    function valid_coord_check(a, b, n_1, n_2) {
        if (0 <= a < n_1 && 0 <= b < n_2) {
            return True
        } else {
            return False
        }
    }

    for (let row = 0; row < nested_array.length; row++) {
        for (let col = 0; col < nested_array[row].length; col++) {
            if (row < nested_array.length - 1) {
                if (nested_array[row][col] == nested_array[row + 1][col]) {
                    neighbors += 1
                }
            }
            if (col < nested_array[row].length - 1) {
                if (nested_array[row][col] == nested_array[row][col + 1]) {
                    neighbors += 1

                }
            }
        }
    }
    return neighbors
}


    console.log(equal_neighbors([
        [2, 2, 5, 7, 4],
        [4, 0, 5, 3, 4],
        [2, 5, 5, 4, 2]]))