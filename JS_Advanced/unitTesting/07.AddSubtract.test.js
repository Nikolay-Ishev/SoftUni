const {expect} = require(`chai`)
const createCalculator = require(`./07.AddSubtract`)


describe (`createCalculator Checker`, () => {
    let instance = null

    //beforeEach will execute in each state on the same level after it
    beforeEach(() => {
        instance = createCalculator()
    })

    it(`has all methods`, () => {
        expect(instance).to.has.ownProperty(`add`)
        expect(instance).to.has.ownProperty(`subtract`)
        expect(instance).to.has.ownProperty(`get`)
    })

    it(`add numbers correctly`, () => {
        instance.add(2)
        instance.add(3)
        expect(instance.get()).to.equal(5)
    })

    it(`subtract numbers correctly`, () => {
        instance.add(10)
        instance.subtract(3)
        instance.subtract(2)
        expect(instance.get()).to.equal(5) 
    })

    it(`add str correctly`, () => {
        instance.add(`2`)
        instance.add(`3`)
        expect(instance.get()).to.equal(5)
    })

    it(`subtract str correctly`, () => {
        instance.add(`10`)
        instance.subtract(`3`)
        instance.subtract(`2`)
        expect(instance.get()).to.equal(5) 
    })
})

