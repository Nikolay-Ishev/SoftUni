function reverse_odds(arr_1) {
    return (arr_1 
        .filter((v, i) => i % 2 == 1)
        .map(x => x *2)
        .reverse()
        .join(" "));
}


console.log(reverse_odds([10, 15, 20, 25]))