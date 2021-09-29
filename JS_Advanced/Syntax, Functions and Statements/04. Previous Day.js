function previous_day(year, month, day) {
    // Date takes the index of a month!
    let dateObj = new Date(year, month - 1, day);

    
    dateObj.setDate(dateObj.getDate()-1);

    let dayResult = dateObj.getDate();
    let monthResult = dateObj.getMonth() + 1;
    let yearResult = dateObj.getFullYear();


    return `${yearResult}-${monthResult}-${dayResult}`;
}

console.log(previous_day(2016, 10, 1))