function solve() {
  function createaEl(obj) {
    const details = [obj["img"], obj["name"], obj["price"], obj["decFactor"]]
    let tr = document.createElement(`TR`)
    let firstTd = document.createElement(`TD`)
    let img = document.createElement(`IMG`)
    img.src = details[0]
    firstTd.appendChild(img)
    tr.appendChild(firstTd)
    console.log(tr)
    for (let i = 1; i < details.length; i++) {
      let tableData = document.createElement(`TD`)
      let paragraph = document.createElement(`P`)
      paragraph.textContent = details[i]
      tableData.appendChild(paragraph)
      tr.appendChild(tableData)
    }
    let lastData = document.createElement(`TD`)
    let input = document.createElement(`INPUT`)
    input.setAttribute("type", "checkbox");
    lastData.appendChild(input)
    tr.appendChild(lastData)
    return tr
  }

  function genInp() {
    for (el of JSON.parse(generateInput.value)) {
      body.appendChild(createaEl(el))
    }
  }

  function buy() {
    const names = []
    let sum = 0
    const decFactors = []
    for (el of Array.from(body.children)) {
      let input = el.getElementsByTagName(`input`)[0]
      if (input.checked) {
        let [name, price, decFactor] = el.getElementsByTagName(`p`)
        names.push(name.textContent)
        sum += parseFloat(price.textContent)
        decFactors.push(parseFloat(decFactor.textContent))
      }
    }
    const avgFactor = decFactors.reduce((a, b) => a + b, 0) / decFactors.length
    buyInput.value = `Bought furniture: ${names.join(", ")}\nTotal price: ${sum.toFixed(2)}\nAverage decoration factor: ${avgFactor}`
  }

  let body = document.getElementsByTagName(`tbody`)[0]
  let [generateButton, buyButton] = document.getElementsByTagName(`button`)
  let [generateInput, buyInput] = document.getElementsByTagName(`textarea`)

  generateButton.addEventListener(`click`, genInp)
  buyButton.addEventListener(`click`, buy)
}