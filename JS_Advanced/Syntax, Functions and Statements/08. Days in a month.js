function number_of_days(month, year) {
    let a = new Date(year, month, 0).getDate()
    console.log(a);
}

number_of_days(1, 2020)