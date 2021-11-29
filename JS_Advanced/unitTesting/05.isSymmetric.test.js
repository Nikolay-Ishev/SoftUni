const {expect} = require(`chai`)
const isSymmetric = require('./05.isSymmetric')


describe (`Symmetry Checker`, () => {
    it(`Return false for any input that isn’t of the correct type`, () => {
        expect(isSymmetric(5)).to.be.false;
        expect(isSymmetric(true)).to.be.false;
        expect(isSymmetric(`string`)).to.be.false;
        expect(isSymmetric({obj: 1})).to.be.false
    })
    it(`Return true if the input array is symmetric`, () => {
        expect(isSymmetric([5])).to.be.true;
        expect(isSymmetric([5, 3, 5])).to.be.true;
        expect(isSymmetric([5, 6, 6, 5])).to.be.true;
        expect(isSymmetric(['5', '6', '6', '5'])).to.be.true;
    })
    it(`Return false if the input array is not symmetric`, () => {
        expect(isSymmetric([5, 6])).to.be.false;
    })
    it(`Return false if the input array is not symmetric due to different types`, () => {
        expect(isSymmetric([5, 6, "5"])).to.be.false
    })
    it(`Return false if the input str array is not symmetric`, () => {
        expect(isSymmetric(["5", "6", "5", "4"])).to.be.false
    })
})
