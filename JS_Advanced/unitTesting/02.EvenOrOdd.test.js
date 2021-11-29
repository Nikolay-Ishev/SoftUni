const {expect} = require(`chai`)
const isOddOrEven = require(`./02.EvenOrOdd`)


describe (`isOddOrEven Checker`, () => {
    it(`returns undefined If the passed parameter is NOT a string.`, () => {
        expect(isOddOrEven(1)).to.equal(undefined)
        expect(isOddOrEven(true)).to.equal(undefined)
        expect(isOddOrEven([1, 2, 3])).to.equal(undefined)
        expect(isOddOrEven({test: 1})).to.equal(undefined)
    })

    it(`returns even where we pass a string with even length`, () => {
        expect(isOddOrEven(`asd`)).to.equal(`odd`)
    })

    it(`returns odd where we pass a string with odd length`, () => {
        expect(isOddOrEven(`asdf`)).to.equal(`even`)
    })
    it(`works corectly when passing multiple different strings in a row`, () => {
        isOddOrEven(`test`)
        isOddOrEven(`testtwo`)
        expect(isOddOrEven(`asdf`)).to.equal(`even`)
        expect(isOddOrEven(`d`)).to.equal(`odd`)
        expect(isOddOrEven(`asdfdds`)).to.equal(`odd`)
    })
})