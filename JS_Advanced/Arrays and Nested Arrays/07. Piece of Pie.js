function pie(arr, pie_1, pie_2) {
    const start = arr.indexOf(pie_1);
    const end = arr.indexOf(pie_2);
    return arr.slice(start, end + 1);
}

console.log(pie(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'))