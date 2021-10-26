function solve() {
    return {
        mage(name) {
            return {
                name,
                health: 100,
                mana: 100,
                cast(spell) {
                    this.mana -= 1
                    console.log(`${this.name} cast ${spell}`)
                }
            }
        },
        fighter(name) {
            return {
                name,
                health: 100,
                stamina : 100,
                fight() {
                    this.stamina -= 1
                    console.log(`${this.name} slashes at the foe!`)
                }
            }
        }
    }
}


function better_solve() {
    // canCast is function which receive state and returns object with method cast
    const canCast = (state) => ({
        cast: (spell) => {
            console.log(`${state.name} cast ${spell}`)
            state.mana--
        }
    })

    const canFight = (state) => ({
        fight: () => {
            console.log(`${state.name} slashes at the foe!`)
            state.stamina--
        }
    })

    const crFighter = (fName) => {
        let state = {
            name: fName,
            health: 100,
            stamina: 100
        }
        //Object.assign(target, ...sources)
        //The Object.assign() method copies all enumerable own properties from one or more source objects to a target object. It returns the modified target object.
        return Object.assign(state, canFight(state))
    }

    const crMage = (mName) => {
        let state = {
            name: mName,
            health: 100,
            mana: 100
        }
        return Object.assign(state, canCast(state))
    }
    return {mage: crMage, fighter: crFighter} 
}


let create = better_solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball")
scorcher.cast("thunder")
scorcher.cast("light")

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight()

console.log(scorcher2.stamina);
console.log(scorcher.mana);