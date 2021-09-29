function words_upper(string_1) {
    let results = string_1.match(/\w+/g);
    console.log(results.join(", ").toUpperCase())
}

words_upper("Hi, how's are you?")