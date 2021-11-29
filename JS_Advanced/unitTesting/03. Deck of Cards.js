function printDeckOfCards(cards) {
    function createCard(face, suit) {
        const faces = [`2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `J`, `Q`, `K`, `A`]
        const suits = {
            'S': '\u2660',
            'H': '\u2665',
            'D': '\u2666',
            'C': '\u2663'
        }
    
        if (faces.includes(face) == false) {
            throw new Error(`Invalid face: ${face}`)
        }
        if (Object.keys(suits).includes(suit) == false) {
            throw new Error(`Invalid suit: ${suit}`)
        } 
        return {
            f: face,
            s: suits[suit],
            toString() {
                return this.f + this.s
            }
        }
    }
    let result = []
    
    
    for (let card of cards) {
        try {
            let suit = card.slice(card.length-1)
            let face = card.slice(0, card.length-1)
            result.push(createCard(face, suit).toString())
            
        } catch (error) {
            return  console.log(`Invalid card: ${card}`)          
        }       
    }
    console.log(result.join(` `)) 
}



printDeckOfCards(['AS', '10D', 'KH', '2C'])
printDeckOfCards(['5S', '3D', 'QD', '1C'])

