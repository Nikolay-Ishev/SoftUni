window.addEventListener('load', solve);

function solve() {
    function isNum(val){
        return !isNaN(val)
    }

    function isEmpty(str) {
        return !str.trim().length;
    }

    const addButton = document.querySelector("#add")
    addButton.type = `button`

    const model = document.querySelector("#model")
    const year = document.querySelector("#year")
    const description = document.querySelector("#description")
    const price = document.querySelector("#price")

    const fList = document.querySelector("#furniture-list")
    const total = document.getElementsByClassName("total-price")[0]
    


    addButton.addEventListener(`click`, function add() {
        if (!isEmpty(model.value) && !isEmpty(description.value) && !isEmpty(year.value) && !isEmpty(price.value) && 
            isNum(year.value) && isNum(price.value) && price.value > 0 && year.value > 0) {
                //create and append main row of element
                const tableRowMain  = document.createElement('tr')
                tableRowMain.className = "info"
                const tdModel = document.createElement('td')
                tdModel.textContent = model.value
                const tdPrice = document.createElement('td')
                tdPrice.textContent = Number(price.value).toFixed(2)
                const tdButtons = document.createElement('td')
                const moreButton = document.createElement('button')
                moreButton.textContent = `More Info`
                moreButton.className = `moreBtn`
                const buyButton = document.createElement(`button`)
                buyButton.textContent = `Buy it`
                buyButton.className = `buyBtn`
                tdButtons.appendChild(moreButton)
                tdButtons.appendChild(buyButton)
                tableRowMain.appendChild(tdModel)
                tableRowMain.appendChild(tdPrice)
                tableRowMain.appendChild(tdButtons)
                fList.appendChild(tableRowMain)

                //create and append second row of element
                const tableRowSecond  = document.createElement('tr')
                tableRowSecond.className = "hide"
                tableRowSecond.style.display = "none"
                const tdYear = document.createElement(`td`)
                tdYear.textContent = `Year: ${year.value}`
                const tdDescr =  document.createElement(`td`)
                tdDescr.colSpan = "3"
                tdDescr.textContent = `Description: ${description.value}`
                tableRowSecond.appendChild(tdYear)
                tableRowSecond.appendChild(tdDescr)
                fList.appendChild(tableRowSecond)

                //moreButton shows second row
                moreButton.addEventListener(`click`, function more() {
                    if (moreButton.textContent == (`More Info`)) {
                        tableRowSecond.style.display = "contents"
                        moreButton.textContent = `Less Info`
                    } else {
                        tableRowSecond.style.display = "none"
                        moreButton.textContent = `More Info`
                    }
                })

                //buyButton functionality
                buyButton.addEventListener(`click`, function buy() {
                    tableRowMain.remove()
                    tableRowSecond.remove()
                    total.textContent = (Number(total.textContent) + Number(tdPrice.textContent)).toFixed(2)
                })

                //clear the input
                model.value = ""
                year.value = ""
                description.value = ""
                price.value = ""
        }
    })
}
