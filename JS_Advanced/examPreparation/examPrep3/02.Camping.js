class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer
        this.location = location
        this.priceForTheCamp = {"child": 150, "student": 300, "collegian": 500}
        this.listOfParticipants = []
    }

    registerParticipant (pName, pCondition, pMoney) {
        if (!this.priceForTheCamp[pCondition]) {
            throw Error("Unsuccessful registration at the camp.")
        }
        for (let p of this.listOfParticipants) {
            if (p.name == pName) {
                return `The ${pName} is already registered at the camp.`
            }
        }
        if (pMoney < this.priceForTheCamp[pCondition]) {
            return `The money is not enough to pay the stay at the camp.`
        }
        else {
            this.listOfParticipants.push({name: pName, condition: pCondition, power: 100, wins: 0})
            return `The ${pName} was successfully registered.`
        }
    }

    unregisterParticipant (pName) {
        for (let p of this.listOfParticipants) {
            if (p.name == pName) {
                const index = this.listOfParticipants.indexOf(p);
                if (index > -1) {
                    this.listOfParticipants.splice(index, 1);
                }
                return `The ${pName} removed successfully.`
            }
        }
        throw Error(`The ${pName} is not registered in the camp.`)
    }

    timeToPlay (typeOfGame, participant1, participant2) {
        if (typeOfGame == "WaterBalloonFights") {
            let validParticipants = 0
            let player1
            let player2
            for (let p of this.listOfParticipants) {
                if (p.name == participant1) {
                    validParticipants += 1
                    player1 = p
                }
                else if (p.name == participant2) {
                    validParticipants += 1
                    player2 = p
                }
            }
            if (validParticipants < 2) {
                throw Error(`Invalid entered name/s.`)
            }
            if (player1.condition != player2.condition) {
                throw Error(`Choose players with equal condition.`)
            }
            if (player1.power > player2.power) {
                player1.wins += 1
                return `The ${player1.name} is winner in the game ${typeOfGame}.`
            }
            else if (player1.power < player2.power) {
                player2.wins += 1
                return `The ${player2.name} is winner in the game ${typeOfGame}.`
            }
            else {return `There is no winner.`}
        }

        else if (typeOfGame == "Battleship") {
            let player1
            for (let p of this.listOfParticipants) {
                if (p.name == participant1) {
                    player1 = p
                }
            }
            if (!player1) {
                throw Error(`Invalid entered name/s.`)
            }
            player1.power += 20
            return `The ${player1.name} successfully completed the game ${typeOfGame}.`
        }
    }

    toString () {
        let result = []
        let numberOfParticipants = this.listOfParticipants.length
        result.push(`${this.organizer} will take ${numberOfParticipants} participants on camping to ${this.location}`)
        this.listOfParticipants.sort((a, b) => b.wins - a.wins)
        for (let p of this.listOfParticipants) {
            result.push(`${p.name} - ${p.condition} - ${p.power} - ${p.wins}`)
        }
        return result.join("\n")
    }
}



const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");

console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.registerParticipant("Dimitur Petrov", "student", 300));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Dimitur Kostov", "Dimitur Petrov"))
console.log(summerCamp + "")