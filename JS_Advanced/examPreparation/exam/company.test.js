const {expect} = require(`chai`)
const companyAdministration = require("./company.js")

describe (`companyAdministration Checker`, () => {
    describe (`hiringEmployee   Checker`, () => {
        it(` throw an error: "We are not looking for workers for this position." If the value of the string position is different from "Programmer"`, () => {
            expect(() => companyAdministration.hiringEmployee(`str`, `wrong`, 5)).to.throws("We are not looking for workers for this position.")
            expect(() => companyAdministration.hiringEmployee(`str2`, 12, 133)).to.throws("We are not looking for workers for this position.")
        })

        it(`return a string If the yearsЕxperience are greater than or equal to 3`, () => {
            expect(companyAdministration.hiringEmployee(`str`, "Programmer", 5)).to.equals(`str was successfully hired for the position Programmer.`)
            expect(companyAdministration.hiringEmployee(`test`, "Programmer", 3)).to.equals(`test was successfully hired for the position Programmer.`)
            expect(companyAdministration.hiringEmployee(`name`, "Programmer", 333)).to.equals(`name was successfully hired for the position Programmer.`)
        })

        it(`return a message if the above conditions are not met`, () => {
            expect(companyAdministration.hiringEmployee(`str`, "Programmer", 2)).to.equals(`str is not approved for this position.`)
            expect(companyAdministration.hiringEmployee(`test`, "Programmer", 0)).to.equals(`test is not approved for this position.`)
            expect(companyAdministration.hiringEmployee(`name`, "Programmer", -5)).to.equals(`name is not approved for this position.`)
            expect(companyAdministration.hiringEmployee(`123`, "Programmer", 1)).to.equals(`123 is not approved for this position.`)
            expect(companyAdministration.hiringEmployee(`1234`, "Programmer", -55)).to.equals(`1234 is not approved for this position.`)
        })
    })

    describe (`calculateSalary  Checker`, () => {
        it(`throw an error: "Invalid hours" if the hours are not a number, or are a negative number`, () => {
            expect(() => companyAdministration.calculateSalary(-1)).to.throws("Invalid hours")
            expect(() => companyAdministration.calculateSalary(-12.5)).to.throws("Invalid hours")
            expect(() => companyAdministration.calculateSalary([1, 2])).to.throws("Invalid hours")
            expect(() => companyAdministration.calculateSalary(true)).to.throws("Invalid hours")
            expect(() => companyAdministration.calculateSalary("str")).to.throws("Invalid hours")
            expect(() => companyAdministration.calculateSalary({"str":-12.5})).to.throws("Invalid hours")
        })

        it(` multipies the pay for one hour (15) by the number of hours`, () => {
            expect(companyAdministration.calculateSalary(0)).to.equals(0)
            expect(companyAdministration.calculateSalary(1)).to.equals(15)
            expect(companyAdministration.calculateSalary(1.5)).to.equals(22.5)
            expect(companyAdministration.calculateSalary(160)).to.equals(2400)

        })

        it(`adds an additional BGN 1000 bonus if the employee has been working for more than 160 hours`, () => {
            expect(companyAdministration.calculateSalary(161)).to.equals(3415)
            expect(companyAdministration.calculateSalary(200)).to.equals(4000)
            expect(companyAdministration.calculateSalary(200.5)).to.equals(4007.5)
        })
    })

    
    describe (`firedEmployee   Checker`, () => {
        it(`throws an error: "Invalid input" if passed employees parameter is not an array`, () => {
            expect(() => companyAdministration.firedEmployee ('wrong', 2)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (2, [1, 2])).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee ({"str": 2}, 5)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee ()).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (false)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (false, {"str": 5})).to.throws("Invalid input")
        })

        it(`throws an error: "Invalid input" If the index is not a number and is outside the limits of the array.`, () => {
            expect(() => companyAdministration.firedEmployee ([1, 2], 2)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (["name1", "name2"], 3)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (["name1", "name2"], -1)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee ([], 1)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (["test", "test2"], -5)).to.throws("Invalid input")
            expect(() => companyAdministration.firedEmployee (["test", "test2"])).to.throws("Invalid input")
        })

        it(`oreturn the changed array of employees as a string, joined by a comma and a space.`, () => {
            expect(companyAdministration.firedEmployee ([1, 2], 0)).to.equals("2")
            expect(companyAdministration.firedEmployee ([1, 2], 1)).to.equals("1")
            expect(companyAdministration.firedEmployee (["test", "test1", "test2"], 0)).to.equals("test1, test2")
            expect(companyAdministration.firedEmployee (["test", "test1", "test2"], 2)).to.equals("test, test1")
            expect(companyAdministration.firedEmployee (["test", "test1", "test2"], 1)).to.equals("test, test2")
        })
    })
})