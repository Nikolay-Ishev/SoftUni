function validate() {
    const validEmail = /^[a-z]+@[a-z]+\.[a-z]+$/gm
    const inputField = document.querySelector(`#email`)
    inputField.addEventListener('change', (event) => {
        if (!inputField.value.match(validEmail)) {
            inputField.classList.add("error")
        } else(inputField.classList.remove("error"))
      });
}