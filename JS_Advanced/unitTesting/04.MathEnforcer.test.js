const {expect} = require(`chai`)
const mathEnforcer = require(`./04.MathEnforcer`)

describe (`MathEnforcer Checker`, () => {
    describe (`addFive Checker`, () => {
        it(`add 5 to the parameter if it is a number and return the result.`, () => {
            expect(mathEnforcer.addFive(5)).to.equal(10)
            expect(mathEnforcer.addFive(5.52322)).to.closeTo(10.52322, 0.01)
            expect(mathEnforcer.addFive(-12)).to.equal(-7)
        })

        it(`works corectly when called multiple times in a row`, () => {
            mathEnforcer.addFive(5)
            mathEnforcer.addFive(10)
            mathEnforcer.addFive(52)
            expect(mathEnforcer.addFive(52)).to.equal(57)
            expect(mathEnforcer.addFive(5.9)).to.equal(10.9)
        })

        it(`returns undefined if the parameter is not a number.`, () => {
            expect(mathEnforcer.addFive(`str`)).to.equal(undefined)
            expect(mathEnforcer.addFive([`str`])).to.equal(undefined)
            expect(mathEnforcer.addFive({test: `test1`})).to.equal(undefined)
        })
    })
    describe (`subtractTen Checker`, () => {
        it(`subtract ten from the parameter if it is a number and return the result.`, () => {
            expect(mathEnforcer.subtractTen(12)).to.equal(2)
            expect(mathEnforcer.subtractTen(5.52322)).to.closeTo(-4.47678, 0.01)
            expect(mathEnforcer.subtractTen(-12)).to.equal(-22)
        })

        it(`works corectly when called multiple times in a row`, () => {
            mathEnforcer.subtractTen(5)
            mathEnforcer.subtractTen(10)
            mathEnforcer.subtractTen(52)
            expect(mathEnforcer.subtractTen(52)).to.equal(42)
            expect(mathEnforcer.subtractTen(5.9)).to.equal(-4.1)
        })

        it(`returns undefined if the parameter is not a number.`, () => {
            expect(mathEnforcer.subtractTen(`str`)).to.equal(undefined)
            expect(mathEnforcer.subtractTen([`str`])).to.equal(undefined)
            expect(mathEnforcer.subtractTen({test: `test1`})).to.equal(undefined)
        })

    })
    describe (`sum Checker`, () => {
        it(`sums two parameters if numbers and return the result.`, () => {
            expect(mathEnforcer.sum(12, 4)).to.equal(16)
            expect(mathEnforcer.sum(5.52322, 4.11)).to.closeTo(9.63322, 0.01)
            expect(mathEnforcer.sum(-12, -10)).to.equal(-22)
        })

        it(`works corectly when called multiple times in a row`, () => {
            mathEnforcer.sum(5, 5)
            mathEnforcer.sum(10, 15)
            mathEnforcer.sum(52, 222222222)
            expect(mathEnforcer.sum(52, 100)).to.equal(152)
            expect(mathEnforcer.sum(5.9, 11.1)).to.equal(17)
        })

        it(`returns undefined if the parameter is not a number.`, () => {
            expect(mathEnforcer.sum(`str`, 2)).to.equal(undefined)
            expect(mathEnforcer.sum([`str`], 2)).to.equal(undefined)
            expect(mathEnforcer.sum({test: `test1`}, 3)).to.equal(undefined)
            expect(mathEnforcer.sum(`str`, `str`)).to.equal(undefined)
            expect(mathEnforcer.sum([`str`], [`str`])).to.equal(undefined)
            expect(mathEnforcer.sum({test: `test1`}, {test: `test1`})).to.equal(undefined)
            expect(mathEnforcer.sum(1, `str`)).to.equal(undefined)
            expect(mathEnforcer.sum([2], [`str`])).to.equal(undefined)
            expect(mathEnforcer.sum(5, {test: `test1`})).to.equal(undefined)
        })

    })
})