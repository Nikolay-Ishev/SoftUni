function diagonal_sum(matrix) {
    const last = matrix.length - 1;
    let sum1 = 0
    let sum2 = 0

    for (let i = 0; i < matrix.length; i++) {
        sum1 += Number(matrix[i][i]);
        sum2 += Number(matrix[i][last - i]);
    }
    return `${sum1} ${sum2}`
}

console.log(diagonal_sum([
    ['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4'],
    ['2', '4', '5', '6', '2']
]))