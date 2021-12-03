function tickets(arr, sortCriteria) {

    class Ticket {
        constructor(destination, price, ticketStatus) {
            this.destination = destination;
            this.price = parseFloat(price);
            this.status = ticketStatus;
        }

        static compare(t1, t2) {
            if (sortCriteria == `destination`) {
                return t1.destination.localeCompare(t2.destination)
            } else if (sortCriteria == `price`) {
                return t1.price -t2.price
            } else {
                return t1.status.localeCompare(t2.status)
            }
        }
    }

    const tickets = []

    for (str of arr) {
        [destination, price, ticketStatus] = str.split(`|`)
        price = parseFloat(price)
        let t = new Ticket(destination, price, ticketStatus)
        tickets.push(t)
    }

    tickets.sort(Ticket.compare)
    return tickets
}

console.log(tickets(['Philadelphia|94.20|available',
'New York City|95.99|available',
'New York City|95.99|sold',
'Boston|126.20|available',
'Philadelphia|132.20|departed',
'Chicago|140.20|available',
'Dallas|144.60|sold',
'New York City|206.20|sold',
'New York City|240.20|departed',
'New York City|305.20|departed'],
'price'))

