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

const typeProduct = document.querySelector("#type-product")
const description = document.querySelector("#description")
const clientName = document.querySelector("#client-name")
const clientPhone = document.querySelector("#client-phone")
const sendBtn = document.querySelector("#right button")
//sendBtn.type = `button`
const receivedOrders = document.querySelector("#received-orders")
const completeOrders = document.querySelector("#completed-orders")
const clearBtn = document.getElementsByClassName("clear-btn")[0]

//create event listener to clear btn
clearBtn.addEventListener(`click`, function clear(){
    const container = Array.from(completeOrders.getElementsByClassName("container"))
    for (let el of container) {
        el.remove()
    }
})

//create event listener to send btn
sendBtn.addEventListener(`click`, function send(e) {
    e.preventDefault()
    if (!isEmpty(description.value) && !isEmpty(clientName.value) && !isEmpty(clientPhone.value)) {
        //create div el and its children
        const newDiv = document.createElement("div")
        newDiv.className = "container"
        const h2 = document.createElement("h2")
        h2.textContent = `Product type for repair: ${typeProduct.value}`
        const h3 = document.createElement("h3")
        h3.textContent = `Client information: ${clientName.value}, ${clientPhone.value}`
        const h4 = document.createElement("h4")
        h4.textContent = `Description of the problem: ${description.value}`
        const startBtn = document.createElement("button")
        const finBtn = document.createElement("button")
        startBtn.className = "start-btn"
        finBtn.className = "finish-btn"
        startBtn.textContent = "Start repair"
        finBtn.textContent = "Finish repair"
        finBtn.disabled = true
        appendChildren([h2, h3, h4, startBtn, finBtn], newDiv)
        receivedOrders.appendChild(newDiv)

        //create event listener to start btn
        startBtn.addEventListener(`click`, function start(){
            startBtn.disabled = true
            finBtn.disabled = false
        })

        //create event listener to finish btn
        finBtn.addEventListener(`click`, function finish(){
            startBtn.remove()
            finBtn.remove()
            completeOrders.appendChild(newDiv)
        })

        // clear input fields
        description.value = ""
        clientName.value = ""
        clientPhone.value = ""
        typeProduct.value = ""
    }
})

}