function string_length(str1, str2, str3) {
    let full_str = str1 + str2 + str3
    str_length = full_str.length
    
    console.log(str_length)
    console.log(Math.floor(str_length / 3))
}

string_length('chocolate', 'ice cream', 'cake')
string_length('pasta', '5', '22.3')