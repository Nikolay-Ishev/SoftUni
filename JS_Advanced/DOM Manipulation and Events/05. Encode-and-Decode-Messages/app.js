function encodeAndDecodeMessages() {
    function encodeClick(ev){
        decodeText.value = encodeString(encodeText.value)
        encodeText.value = ''
    }
    function decodeClick(ev) {
        decodeText.value = decodeString(decodeText.value)
    }
    function encodeString(str) {
        const arr = []
        for (let i=0; i<str.length;i++) {
            arr.push(String.fromCharCode(str.charCodeAt(i) + 1))
        }
        return arr.join("")
    }
    function decodeString(str) {
        const arr = []
        for (let i=0; i<str.length;i++) {
            arr.push(String.fromCharCode(str.charCodeAt(i) - 1))
        }
        return arr.join("")
    }

    const main = document.getElementById(`main`)
    let encodeText
    let decodeText

    for (let menu of Array.from(main.children)) {
        const button = menu.getElementsByTagName(`button`)[0]
        if (button.textContent == `Encode and send it`) {
            button.addEventListener(`click`, encodeClick)
            encodeText = menu.getElementsByTagName(`textarea`)[0]
        } else if (button.textContent == `Decode and read it`) {
            button.addEventListener(`click`, decodeClick)
            decodeText = menu.getElementsByTagName(`textarea`)[0]
        }
    }

}