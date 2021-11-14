function lockedProfile() {
    const content = document.getElementById(`main`)
    content.addEventListener(`click`, onClick)

    function onClick(ev) {
        if (ev.target.tagName == `BUTTON`) {
            const profile = ev.target.parentNode

            // .find(d => d.id.includes(`HiddenFields`));
            const hiddenEl = profile.getElementsByTagName(`div`)[0]


            const button = profile.getElementsByTagName(`button`)[0]
            if (profile.querySelector(`input[value="unlock"]`).checked) {
                if (button.textContent == `Show more`) {
                    hiddenEl.style.display = `block`
                    button.textContent = "Hide it"
                } else {
                    hiddenEl.style.display = ``
                    button.textContent = `Show more`
                }
            } 
        }
    }
}