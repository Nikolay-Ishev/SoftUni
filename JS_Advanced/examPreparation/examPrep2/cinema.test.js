const {expect} = require(`chai`)
const cinema = require("./cinema.js")

describe (`cinema Checker`, () => {
    describe (`showMovies Checker`, () => {
        it(`returns the string If the length of the input array is zero`, () => {
            expect(cinema.showMovies([])).to.equals("There are currently no movies to show.")
        })

        it(`returns a string of available movies, separated by a comma and space`, () => {
            expect(cinema.showMovies(["King Kong", "The Tomorrow War", "Joker"])).to.equals("King Kong, The Tomorrow War, Joker")
            expect(cinema.showMovies(['test1', 'test2'])).to.equals("test1, test2")
        })    
    })

    describe (`ticketPrice Checker`, () => {
        it(` return the price according to the type If present in the schedule`, () => {
            expect(cinema.ticketPrice("Premiere")).to.equals(12.00)
            expect(cinema.ticketPrice("Normal")).to.equals(7.50)
            expect(cinema.ticketPrice("Discount")).to.equals(5.50)
            expect(cinema.ticketPrice("Premiere")).to.equals(12.00)
            expect(cinema.ticketPrice("Normal")).to.equals(7.50)
            expect(cinema.ticketPrice("Discount")).to.equals(5.50)
        })

        it(`throws an error in the following format "Invalid projection type." if wrong type.`, () => {
            expect(() => cinema.ticketPrice(`str`)).to.throws('Invalid projection type.')
            expect(() => cinema.ticketPrice(`str2`)).to.throws('Invalid projection type.')

        })
    })

    
    describe (`swapSeatsInHall Checker`, () => {
        it(`swaps the seat number in the cinema hall, when two numbers are submitted`, () => {
            expect(cinema.swapSeatsInHall(1, 2)).to.equals("Successful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(5, 20)).to.equals("Successful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(5, 10)).to.equals("Successful change of seats in the hall.")
        })

        it(` is not successful If one of the two numbers do not exist`, () => {
            expect(cinema.swapSeatsInHall(2)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall()).to.equals("Unsuccessful change of seats in the hall.")
        })

        it(` is not successful If The numbers are not integers`, () => {
            expect(cinema.swapSeatsInHall(2, true)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall([], 5)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall({2: `str`}, true)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(`str`, 5)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(2.12, 5.17)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(1.5, 5)).to.equals("Unsuccessful change of seats in the hall.")
        })

        it(`is not successful If one of the numbers is greater than the capacity of the hall – 20`, () => {
            expect(cinema.swapSeatsInHall(2, 21)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(7, 77)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(77, 8)).to.equals("Unsuccessful change of seats in the hall.")
        })

        it(`is not successful If Seats are less or equal of 0`, () => {
            expect(cinema.swapSeatsInHall(2, -21)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(-7, 15)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(-77, -8)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(0, 8)).to.equals("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(12, 0)).to.equals("Unsuccessful change of seats in the hall.")
        })
    })
})