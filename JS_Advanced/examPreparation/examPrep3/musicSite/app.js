window.addEventListener('load', solve);

function solve() {
    function isNum(val){
        return !isNaN(val)
    }

    function isEmpty(str) {
        return !str.trim().length;
    }

    function appendChildren(arr, parent) {
        for (el of arr) {
            parent.appendChild(el)
        }
    }

    const addButton = document.querySelector("#add-btn")
    addButton.type = `button`
    const genreInput = document.querySelector("#genre")
    const nameInput = document.querySelector("#name")
    const authorInput = document.querySelector("#author")
    const dateInput = document.querySelector("#date")
    const allHitsContainer = document.getElementsByClassName("all-hits-container")[0]
    const likesPara = document.getElementsByClassName("likes")[0]
    const likes = likesPara.getElementsByTagName("p")[0]
    const savedDiv = document.getElementsByClassName("saved-container")[0]

    addButton.addEventListener(`click`, function add() {
        if (!isEmpty(genreInput.value) && !isEmpty(nameInput.value) && !isEmpty(authorInput.value) && !isEmpty(dateInput.value)) {
            //create div el and its children
            const newDiv = document.createElement("div")
            newDiv.className = "hits-info"
            const newImg = document.createElement("img")
            newImg.src = "./static/img/img.png"
            const h2Genre = document.createElement("h2")
            h2Genre.textContent = `Genre: ${genreInput.value}`
            const h2Name = document.createElement("h2")
            h2Name.textContent = `Name: ${nameInput.value}`
            const h2Author = document.createElement("h2")
            h2Author.textContent = `Author: ${authorInput.value}`
            const h3Date = document.createElement("h3")
            h3Date.textContent = `Date: ${dateInput.value}`
            const saveBtn = document.createElement("button")
            const likeBtn = document.createElement("button")
            const delBtn = document.createElement("button")
            saveBtn.className = "save-btn"
            likeBtn.className = "like-btn"
            delBtn.className = "delete-btn"
            saveBtn.textContent = "Save song"
            likeBtn.textContent = "Like song"
            delBtn.textContent = "Delete"
            appendChildren([newImg, h2Genre, h2Name, h2Author, h3Date, saveBtn, likeBtn, delBtn], newDiv)

            //create event listener for del button
            delBtn.addEventListener(`click`, function delBut() {
                newDiv.remove()
            })

            //create event listener for the like and save buttons
            newDiv.addEventListener(`click`, function onClick(e) {
                //like button
                if (e.target.tagName.toLowerCase() === 'button' && e.target.textContent === "Like song") {
                    let [info1, info2,  l] = likes.textContent.split(" ")
                    likes.textContent = info1 + " " + info2 + " " + (Number(l) + 1)
                    e.target.disabled = true
                }
                //save button
                else if (e.target.tagName.toLowerCase() === 'button' && e.target.textContent === "Save song") {
                    saveBtn.remove()
                    likeBtn.remove()
                    savedDiv.appendChild(newDiv)
                }
            })

            //append the div el to all hits container
            allHitsContainer.appendChild(newDiv)

            //clear input
            genreInput.value = ""
            nameInput.value = ""
            authorInput.value = ""
            dateInput.value = ""

        }
    })
}