class Movie {
    constructor (movieName, ticketPrice) {
        this.movieName = movieName
        this.ticketPrice = Number(ticketPrice)
        this.screenings = []
        this.totalProfit = 0
        this.totalSoldTickets = 0
    }

    newScreening(scrDate, scrHall, ScrDescription) {
        for (let scr of this.screenings) {
            if (scr.date === scrDate && scr.hall === scrHall) {
                throw Error(`Sorry, ${scrHall} hall is not available on ${scrDate}`)
            }
        }
        this.screenings.push({date: scrDate, hall: scrHall, description: ScrDescription})
        return `New screening of ${this.movieName} is added.`
    }

    endScreening(scrDate, scrHall, soldTickets) {
        for (let scr of this.screenings) {
            if (scr.date === scrDate && scr.hall === scrHall) {
                let currentProfit = soldTickets * this.ticketPrice
                this.totalProfit += currentProfit
                this.totalSoldTickets += soldTickets

                const index = this.screenings.indexOf(scr)
                this.screenings.splice(index, 1)

                return `${this.movieName} movie screening on ${scrDate} in ${scrHall} hall has ended. Screening profit: ${currentProfit}`
            }   
        }
        throw Error(`Sorry, there is no such screening for ${this.movieName} movie.`)
    }

    toString() {
        const result = []
        result.push(`${this.movieName} full information:`)
        result.push(`Total profit: ${this.totalProfit.toFixed(0)}$`)
        result.push(`Sold Tickets: ${this.totalSoldTickets}`)
        if (this.screenings.length > 0) {
            this.screenings.sort(function(a, b){return a.hall.localeCompare(b.hall)})
            result.push("Remaining film screenings:")
            for (let scr of this.screenings) {
                result.push(`${scr.hall} - ${scr.date} - ${scr.description}`)
            }
        } else {result.push("No more screenings!")}
        return result.join(`\n`)
    }
}

let m = new Movie('Wonder Woman 1984', '10.00');
console.log(m.newScreening('October 2, 2020', 'IMAX 3D', `3D`));
console.log(m.newScreening('October 2, 2020', 'IMAX 3D', `3D`));
