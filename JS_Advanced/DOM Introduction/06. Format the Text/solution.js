function solve() {
  const inputArr = Array.from(document.getElementById("input").value.split("."))
  const output = document.getElementById("output")
  output.innerHTML = ""
  let paragraph = []
  for (let i=0;i<inputArr.length - 1;i++) {
    if (inputArr[i].length < 1) {continue}

    paragraph.push(inputArr[i])
    if (i==inputArr.length - 2 || paragraph.length == 3) {
      const newP = document.createElement("p")
      const newContent = document.createTextNode(paragraph.join(".") + ".")
      newP.appendChild(newContent)
      output.appendChild(newP)
      paragraph.length = 0
    }
  }
}



