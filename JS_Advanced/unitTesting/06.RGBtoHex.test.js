const {expect} = require(`chai`)
const rgbToHexColor = require(`./06.RGBtoHex`)


describe (`rgbToHexColor Checker`, () => {
    it(`Return undefined if red parameter is of an invalid type`, () => {
        expect(rgbToHexColor(`a`, 2, 3)).to.equal(undefined)
    })
    it(`Return undefined if green parameter is of an invalid type`, () => {
        expect(rgbToHexColor(2, true, 3)).to.equal(undefined)
    })
    it(`Return undefined if blue parameters is of an invalid type`, () => {
        expect(rgbToHexColor(3, 2, [3])).to.equal(undefined)
    })
    it(`Return undefined if any of the parameters are not in the expected range`, () => {
        expect(rgbToHexColor(-2, 2, 3)).to.equal(undefined)
        expect(rgbToHexColor(2, 2222, 3)).to.equal(undefined)
        expect(rgbToHexColor(2, 5, 256)).to.equal(undefined)
    })
    it(`Return the same color in hexadecimal format as a string`, () => {
        expect(rgbToHexColor(255, 255, 0)).to.equal(`#FFFF00`)
        expect(rgbToHexColor(0, 255, 0)).to.equal(`#00FF00`)
        expect(rgbToHexColor(255, 0, 0)).to.equal(`#FF0000`)
    })
})