function solve() {
    function isNum(val){
        return !isNaN(val)
    }

    function isEmpty(str) {
        return !str.trim().length;
    }

    const container = document.getElementById(`container`)
    const name = container.querySelector('[placeholder="Name"]')
    const age = container.querySelector('[placeholder="Age"]')
    const kind = container.querySelector('[placeholder="Kind"]')
    const currentOwner = container.querySelector('[placeholder="Current Owner"]')
    const add = container.querySelector('button')
    const adoption = document.querySelector("#adoption")
    const adoptionUl = document.querySelector("#adoption ul")
    const adoptedUl = document.querySelector("#adopted ul")
    const adopted = document.querySelector("#adopted")
    add.type = `button`


    add.addEventListener("click", function addPet() {
        if (!isEmpty(name.value) && !isEmpty(age.value) && isNum(age.value) && !isEmpty(kind.value) && !isEmpty(currentOwner.value)) {
            //create para and ints children
            const para = document.createElement("p");

            const x = document.createElement("STRONG")
            x.textContent = name.value

            const node1 = document.createTextNode(" is a ");
            
            const y = document.createElement("STRONG")
            y.textContent = age.value

            const node2 = document.createTextNode(" year old ");

            const z = document.createElement("STRONG")
            z.textContent = kind.value

            para.appendChild(x)
            para.appendChild(node1)
            para.appendChild(y)
            para.appendChild(node2)
            para.appendChild(z)

            //create span
            const ownerSpan = document.createElement('span')
            ownerSpan.textContent = `Owner: ${currentOwner.value}`

            //create button
            const btn = document.createElement("button");
            btn.textContent = `Contact with owner`

            //create li element and append its children
            const li = document.createElement("li");
            li.appendChild(para)
            li.appendChild(ownerSpan)
            li.appendChild(btn)

            //append li to adoption
            adoptionUl.appendChild(li)

            name.value = ""
            age.value = ""
            kind.value = ""
            currentOwner.value = ""
        }
    })

    adoption.addEventListener(`click`, function contactOwner(e) {
        if (e.target.tagName.toLowerCase() === 'button' && e.target.textContent === `Contact with owner`) {
            const newDiv = document.createElement("div")
            const newInput = document.createElement("input")
            newInput.placeholder = "Enter your names"
            const newBtn = document.createElement("button");
            newBtn.textContent = `Yes! I take it!`
            newDiv.appendChild(newInput)
            newDiv.appendChild(newBtn)
            console.log(e.target.parentNode)
            e.target.parentNode.replaceChild(newDiv, e.target)
        }

        else if(e.target.tagName.toLowerCase() === 'button' && e.target.textContent === `Yes! I take it!`) {
            const currentInput = e.target.parentNode.querySelector("input")
            if (!isEmpty(currentInput.value)) {
                const currentLi = e.target.parentNode.parentNode
                const currentSpan = currentLi.querySelector("span")
                const currentDiv = currentLi.querySelector("div")
                currentSpan.textContent = `New Owner: ${currentInput.value}`

                const currentBtn = document.createElement("button");
                currentBtn.textContent = `Checked`
                currentLi.replaceChild(currentBtn, currentDiv)
                adoptedUl.appendChild(currentLi)
            }
        }
    })

    adopted.addEventListener(`click`, function cheked(e) {
        if (e.target.tagName.toLowerCase() === 'button' && e.target.textContent === `Checked`) {
            e.target.parentNode.remove()
        }
    })
}

