const {expect} = require(`chai`)
const testNumbers = require("./testNumbers.js")


describe (`testNumbers Checker`, () => {
    describe (`sumNumbers Checker`, () => {
        it(`sum positive numbers correctly`, () => {
            expect(testNumbers.sumNumbers(2, 2.5)).to.equals(`4.50`)
            expect(testNumbers.sumNumbers(5, 2)).to.equals(`7.00`)
            expect(testNumbers.sumNumbers(5, 5.88)).to.equals(`10.88`)
            expect(testNumbers.sumNumbers(5.555, 3.005)).to.equals(`8.56`)
        })

        it(`sum negative numbers correctly`, () => {
            expect(testNumbers.sumNumbers(-2, 2.5)).to.equals(`0.50`)
            expect(testNumbers.sumNumbers(-5, 2)).to.equals(`-3.00`)
            expect(testNumbers.sumNumbers(5, -5.88)).to.equals(`-0.88`)
            expect(testNumbers.sumNumbers(5.555, -3.005)).to.equals(`2.55`)
        })

        it(`return undefined if the parameters aren't numbers`, () => {
            expect(testNumbers.sumNumbers([1, 2], 2.5)).to.equals(undefined)
            expect(testNumbers.sumNumbers(`test`, 2)).to.equals(undefined)
            expect(testNumbers.sumNumbers(false, -5.88)).to.equals(undefined)
            expect(testNumbers.sumNumbers(5.555, {"test": 1})).to.equals(undefined)
            expect(testNumbers.sumNumbers(true, {"test": 1})).to.equals(undefined)
        })
    
    })

    describe (`numberChecker Checker`, () => {
        it(`throws an error If the input is not a number`, () => {
            expect(() => testNumbers.numberChecker(`str`)).to.throws('The input is not a number!')
            expect(() => testNumbers.numberChecker([1, 2])).to.throws('The input is not a number!')
            expect(() => testNumbers.numberChecker({"test": 1})).to.throws('The input is not a number!')
            expect(() => testNumbers.numberChecker()).to.throws('The input is not a number!')
        })

        it(`checks if it is even`, () => {
            expect(testNumbers.numberChecker(2)).to.equals("The number is even!")
            expect(testNumbers.numberChecker(6)).to.equals("The number is even!")
            expect(testNumbers.numberChecker(-4)).to.equals("The number is even!")
            expect(testNumbers.numberChecker(0)).to.equals("The number is even!")
        })

        it(`checks if it is odd`, () => {
            expect(testNumbers.numberChecker(5)).to.equals("The number is odd!")
            expect(testNumbers.numberChecker(4.5)).to.equals("The number is odd!")
            expect(testNumbers.numberChecker(6.7)).to.equals("The number is odd!")
            expect(testNumbers.numberChecker(-5)).to.equals("The number is odd!")
        })
    })

    
    describe (`averageSumArray Checker`, () => {
        it(`iterates through each element in the array, calculates the sum, and returns the average sum`, () => {
            expect(testNumbers.averageSumArray([1, 2, 3])).to.equals(2)
            expect(testNumbers.averageSumArray([1, -2, 4])).to.equals(1)
            expect(testNumbers.averageSumArray([-1, -2, 0])).to.equals(-1)
        })
    })
})

