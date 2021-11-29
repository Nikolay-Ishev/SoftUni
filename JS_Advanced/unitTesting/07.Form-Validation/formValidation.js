function validate() {
    const mailFormat = /^[^@.]+@[^@]*\.[^@]*$/
    const nameFormat = /^[A-Za-z0-9]{3,20}$/
    const passFormat = /^[A-Za-z0-9_]{5,15}$/

    const nameInput = document.querySelector(`#username`)
    const emailInput = document.querySelector(`#email`)
    const passInput = document.querySelector(`#password`)
    const confirmPassInput = document.querySelector(`#confirm-password`)
    const companyCheckbox = document.querySelector(`#company`)
    const companyInfo = document.querySelector(`#companyInfo`)
    const submitButton = document.querySelector(`#submit`)
    submitButton.type = `button`
    const companyNumber = document.querySelector(`#companyNumber`)
    const validDiv = document.querySelector(`#valid`)
    

    companyCheckbox.addEventListener('change', (companyCheckboxEvent) => {
        if (companyCheckbox.checked) {
            companyInfo.style.display = `block`
        } else {
            companyInfo.style.display = `none`
        }
    });

    submitButton.addEventListener(`click`, (onClick) => {
        let validInfo = true

        function validator(bool, element) {
            if (bool){
                element.style.border = `none`
            } else {
                element.style.border = ``
                element.style.borderColor = `red`
                validInfo = false
            }
        }
        
        if (companyCheckbox.checked) {
            let number = companyNumber.value
            let check = (1000 <= number && number <= 9999)
            validator(check, companyNumber)
        }

        const passMatch = confirmPassInput.value === passInput.value

        validator(new RegExp(nameFormat).test(nameInput.value), nameInput)
        validator(new RegExp(mailFormat).test(emailInput.value) , emailInput)
        validator(passMatch && new RegExp(passFormat).test(passInput.value), passInput)
        validator(passMatch && new RegExp(passFormat).test(passInput.value), confirmPassInput)
        
        if (validInfo) {
            validDiv.style.display = `block`
            console.log(`show`)
        } else {validDiv.style.display = `none`
                console.log(`nope`)    
        }
    })
}
