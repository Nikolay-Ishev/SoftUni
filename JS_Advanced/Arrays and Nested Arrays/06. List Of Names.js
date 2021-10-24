function sorted_names(arr) {
    sorted_arr = arr.sort((a, b) => a.localeCompare(b))
    for (let i=0; i<sorted_arr.length; i++) {
        console.log(`${i+1}.${sorted_arr[i]}`)
    }
}

sorted_names(["John", "Bob", "Christina", "Ema"])