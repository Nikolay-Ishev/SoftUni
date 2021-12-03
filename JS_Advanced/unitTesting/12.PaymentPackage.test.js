const {expect} = require(`chai`)
const PaymentPackage = require(`./12.PaymentPackage`)

describe (`PaymentPackage Checker`, () => {
    let package = null

    //beforeEach will execute in each state on the same level after it
    beforeEach(() => {
        package = new PaymentPackage("Nikolay", 1000);
    })

    it(`has atributes set correctly`, () => {
        expect(package.name).to.equal(`Nikolay`)
        expect(package.value).to.equal(1000)
    })

    it(`is able to get and set the value of the name`, () => {
        expect(package.name).to.equal("Nikolay")
        package.name = `Peter`
        expect(package.name).to.equal("Peter")
    })

    it(`is able to get and set the value of value`, () => {
        expect(package.value).to.equal(1000)
        package.value = 1250
        expect(package.value).to.equal(1250)
        package.value = 0
        expect(package.value).to.equal(0)
    })

    it(`is able to get and set the value of VAT`, () => {
        expect(package.VAT).to.equal(20)
        package.VAT = 30
        expect(package.VAT).to.equal(30)
    })

    it(`is able to get and set the value of active`, () => {
        expect(package.active).to.equal(true)
        package.active = false
        expect(package.active).to.equal(false)
    })

    it(`returns a string, containing an overview of the instance`, () => {      
        expect(package.active).to.equal(true)
        const output = [
            `Package: Nikolay`,
            `- Value (excl. VAT): 1000`,
            `- Value (VAT 20%): 1200`
          ];
        expect(package + "").to.equal(output.join(`\n`)) 
    })

    it(`append the label "(inactive)" to the printed name if the package is not active`, () => {  
        package.active = false    
        expect(package.active).to.equal(false)
        const output = [
            `Package: Nikolay (inactive)`,
            `- Value (excl. VAT): 1000`,
            `- Value (VAT 20%): 1200`
          ];
        expect(package + "").to.equal(output.join(`\n`)) 
    })

    it(`throws error if name is not non empty string`, () => {      
        expect(() => package.name = true).to.throw()
        expect(() => package.name = "").to.throw()
        expect(() => package.name = 2).to.throw()
        expect(() => package.name = [1, 2]).to.throw()
    })

    it(`throws error if value is not non negative number`, () => {      
        expect(() => package.value = true).to.throw()
        expect(() => package.value = "asd").to.throw()
        expect(() => package.value = -2).to.throw()
        expect(() => package.value = [1, 2]).to.throw()
    })

    it(`throws error if VAT is not non negative number`, () => {      
        expect(() => package.VAT = true).to.throw()
        expect(() => package.VAT = "asd").to.throw()
        expect(() => package.VAT = -2).to.throw()
        expect(() => package.VAT = [1, 2]).to.throw()
    })

    it(`throws error if active is not boolean`, () => {      
        expect(() => package.active = 1).to.throw()
        expect(() => package.active = "asd").to.throw()
        expect(() => package.active = -2).to.throw()
        expect(() => package.active = [1, 2]).to.throw()
    })

})