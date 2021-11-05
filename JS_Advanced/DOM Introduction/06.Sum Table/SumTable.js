function sumTable() {
    const elements = document.querySelectorAll(`table tbody tr td:nth-child(even)`)
    let sum = 0
    for (let i=0; i<elements.length - 1;i++) {
        sum += Number(elements[i].textContent)
    }
    console.log(sum)
    //let total = document.getElementById('sum')
    let total = elements[elements.length - 1]
    total.textContent = sum
}