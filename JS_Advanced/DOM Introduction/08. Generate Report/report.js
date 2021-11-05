function generateReport() {
    const rowArr = Array.from(document.getElementsByTagName('tr'))
    const thInputs = Array.from(document.querySelectorAll(`tr input`))
    const headerRow = rowArr[0].children
    const result = []
    for (let i=1;i<rowArr.length;i++) {
        let obj = {}
        const elArr = Array.from(rowArr[i].children)
        for (let ind=0;ind<elArr.length;ind++) {
            if (thInputs[ind].checked) {
                obj[thInputs[ind].name] = elArr[ind].textContent
            }
        }
        result.push(obj)
    }
    document.getElementById("output").textContent = JSON.stringify(result)
}