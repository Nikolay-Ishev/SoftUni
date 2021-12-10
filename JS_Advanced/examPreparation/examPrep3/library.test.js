const {expect} = require(`chai`)
const library = require("./library.js")

describe (`library Checker`, () => {
    describe (`calcPriceOfBook   Checker`, () => {
        it(`throw an error: "Invalid input" if nameOfBook is not a string, or the year is not an integer number`, () => {
            expect(() => library.calcPriceOfBook(`str`, `wrong`)).to.throws("Invalid input")
            expect(() => library.calcPriceOfBook(`str2`, false)).to.throws("Invalid input")
            expect(() => library.calcPriceOfBook([1, 2], 123)).to.throws("Invalid input")
            expect(() => library.calcPriceOfBook(1.5, 22)).to.throws("Invalid input")
            expect(() => library.calcPriceOfBook(`str`, 5.55)).to.throws("Invalid input")
            expect(() => library.calcPriceOfBook({"str": 1}, false)).to.throws("Invalid input")
        })

        it(`calculates price of the book and return: "Price of {nameOfBook} is {price}"`, () => {
            expect(library.calcPriceOfBook(`str`, 1981)).to.equals(`Price of str is 20.00`)
            expect(library.calcPriceOfBook(`test`, 2002)).to.equals(`Price of test is 20.00`)
        })

        it(`is a 50% percent discount from the standard price If the year of publication is less than or equal to 1980`, () => {
            expect(library.calcPriceOfBook(`str`, 1980)).to.equals(`Price of str is 10.00`)
            expect(library.calcPriceOfBook(`test`, 1002)).to.equals(`Price of test is 10.00`)
        })
    })

    describe (`findBook  Checker`, () => {
        it(`throw an error If the length of the booksArr array is zero`, () => {
            expect(() => library.findBook([], 'book')).to.throws("No books currently available")
            expect(() => library.findBook([], "Normal")).to.throws("No books currently available")
        })

        it(`returns: "We found the book you want." If present in the array`, () => {
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "Troy")).to.equals("We found the book you want.")
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "Life Style")).to.equals("We found the book you want.")

        })

        it(`returns: "The book you are looking for is not here!" If not present in the array`, () => {
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "Test")).to.equals("The book you are looking for is not here!")
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "Test2")).to.equals("The book you are looking for is not here!")
        })
    })

    
    describe (`arrangeTheBooks  Checker`, () => {
        it(`throws an error: "Invalid input" if the countBooks is not an integer number, or is a negative number`, () => {
            expect(() => library.arrangeTheBooks(-1)).to.throws("Invalid input")
            expect(() => library.arrangeTheBooks(7.55)).to.throws("Invalid input")
            expect(() => library.arrangeTheBooks(`str`)).to.throws("Invalid input")
            expect(() => library.arrangeTheBooks([5, 10])).to.throws("Invalid input")
            expect(() => library.arrangeTheBooks(false)).to.throws("Invalid input")
            expect(() => library.arrangeTheBooks({"str": 5})).to.throws("Invalid input")
        })

        it(`return: "Great job, the books are arranged." If all the books are arranged on the shelves`, () => {
            expect(library.arrangeTheBooks(40)).to.equals("Great job, the books are arranged.")
            expect(library.arrangeTheBooks(12)).to.equals("Great job, the books are arranged.")
        })

        it(`return: "Insufficient space, more shelves need to be purchased" if no space has been reached`, () => {
            expect(library.arrangeTheBooks(41)).to.equals("Insufficient space, more shelves need to be purchased.")
            expect(library.arrangeTheBooks(112)).to.equals("Insufficient space, more shelves need to be purchased.")
        })
    })
})