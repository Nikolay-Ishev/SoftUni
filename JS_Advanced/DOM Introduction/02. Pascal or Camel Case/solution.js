function solve() {
  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  const text = document.getElementById(`text`)
  const conv = document.getElementById("naming-convention")
  let result = document.getElementById("result")
  if (conv.value != "Camel Case" && conv.value != "Pascal Case") {
    result.textContent = "Error!"
    return
  }
  textArr = text.value.toLowerCase().split(" ")
  for (let i=0;i<textArr.length;i++) {
    if (conv.value == "Camel Case" && i==0) {
      continue
    }
    textArr[i] = capitalizeFirstLetter(textArr[i])
  }
  result.textContent = textArr.join("")
}