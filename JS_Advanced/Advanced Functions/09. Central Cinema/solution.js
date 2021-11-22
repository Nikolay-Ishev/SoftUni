function solve() {
    const movies = document.querySelector(`#movies ul`)
    const archive = document.querySelector("#archive ul")
    const addMovieForm = document.getElementById('container')
    let [name, hall, price, onScrButton] = Array.from(addMovieForm.children);
    onScrButton.type = "button"
    onScrButton.addEventListener(`click`, onScreen)
    const clearButton = document.querySelector(`#archive button`)
    clearButton.type = "button"
    clearButton.addEventListener(`click`, function clear(){
        archive.textContent = ``
    })

    function onScreen(e) {
        e.preventDefault()
        const numPrice = parseFloat(price.value)
        if (!isNaN(numPrice) && name.value !== "" && hall.value !== "") {
            const movie = document.createElement(`li`)
            const hallStr = `Hall: ${hall.value}`
            movie.innerHTML =
                `<span>${name.value}</span>
                <strong>${hallStr}</strong>
                <div>
                    <strong>${numPrice.toFixed(2)}</strong>
                    <input placeholder="Tickets Sold">
                    <button type="button">Archive</button>
                </div>`
            const button = movie.querySelector(`div button`)
            let saveName = name.value
            name.value = ""
            hall.value = ""
            price.value = ""
            button.addEventListener(`click`, function addToArchive(e) {
                let ticketsSold = parseFloat(e.target.parentElement.querySelector(`input`).value)
                if (!isNaN(ticketsSold)) {
                    const archEl = document.createElement(`li`)
                    const total = `Total amount: ${(ticketsSold * numPrice).toFixed(2)}`
                    archEl.innerHTML = 
                    `<span>${saveName}</span>
                    <strong>${total}</strong>
                    <button type="button">Delete</button>`
                    const deleteButton = archEl.querySelector(`button`)
                    deleteButton.addEventListener(`click`, function removeEl() {
                        archEl.remove()
                    })
                    archive.appendChild(archEl)
                    movie.remove()
                }
            })    
            movies.appendChild(movie)
        }          
    }
}
