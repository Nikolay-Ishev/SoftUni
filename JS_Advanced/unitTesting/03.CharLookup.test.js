const {expect} = require(`chai`)
const lookupChar = require(`./03.CharLookup`)

describe (`lookupChar Checker`, () => {
    it(`returns undefined If the first parameter is NOT a string`, () => {
        expect(lookupChar(1, 1)).to.equal(undefined)
        expect(lookupChar([1], 1)).to.equal(undefined)
        expect(lookupChar(false, 1)).to.equal(undefined)
        expect(lookupChar({test:`test1`}, 1)).to.equal(undefined)
    })

    it(`returns undefined If the second parameter is NOT an integer.`, () => {
        expect(lookupChar(`test`, 1.22)).to.equal(undefined)
        expect(lookupChar(`test`, true)).to.equal(undefined)
        expect(lookupChar(`test`, [`asd`])).to.equal(undefined)
        expect(lookupChar(`test`, {test:`test1`})).to.equal(undefined)
    })

    it(`returns "Incorrect index" when index is out of range`, () => {
        expect(lookupChar(`test`, 4)).to.equal("Incorrect index")
        expect(lookupChar(`test`, 14)).to.equal("Incorrect index")
        expect(lookupChar(`test`, -4)).to.equal("Incorrect index")
    })
    it(`return the character at the specified index in the string if parameters are of correct type and values`, () => {
        expect(lookupChar(`test`, 3)).to.equal("t")
        expect(lookupChar(`test`, 2)).to.equal("s")
        expect(lookupChar(`test`, 0)).to.equal("t")
    })
    it(`return the the correct char if called multiple times`, () => {
        lookupChar(`test`, 3)
        lookupChar(`test`, 5)
        lookupChar(`test`, 7)
        expect(lookupChar(`test`, 3)).to.equal("t")
        expect(lookupChar(`test`, 2)).to.equal("s")
        expect(lookupChar(`test`, 0)).to.equal("t")
    })
})