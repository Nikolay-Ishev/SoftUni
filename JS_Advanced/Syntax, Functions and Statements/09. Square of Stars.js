function square_of_stars() {
    if (typeof arguments[0] === "undefined") {
        stars_n = 5
    } else stars_n = arguments[0]
    for (let i = 0; i<stars_n; i++) {
        square_row =  "* ".repeat(stars_n - 1) + "*"
        console.log(square_row)
    }
}

square_of_stars()
square_of_stars(2)
square_of_stars(5)
square_of_stars(1)