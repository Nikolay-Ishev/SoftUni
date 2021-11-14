function attachEventsListeners2() {
    content = document.getElementsByTagName(`main`)[0]
    content.addEventListener(`click`, onClick)

    function onClick(ev) {
        if (ev.target.type == `button`) {
            const id = ev.target.id
            if (id == "secondsBtn") {
                seconds = Number(document.getElementById(`seconds`).value)
                document.getElementById(`minutes`).value = seconds / 60
                document.getElementById(`hours`).value = seconds / 3600 
                document.getElementById(`days`).value = seconds / 3600 / 24
            }
            if (id == "minutesBtn") {
                minutes = Number(document.getElementById(`minutes`).value)
                document.getElementById(`seconds`).value = minutes * 60
                document.getElementById(`hours`).value = minutes / 60 
                document.getElementById(`days`).value = minutes / 60 / 24
            }
            if (id == "hoursBtn") {
                hours = Number(document.getElementById(`hours`).value)
                document.getElementById(`minutes`).value = hours * 60
                document.getElementById(`seconds`).value = hours * 3600 
                document.getElementById(`days`).value = hours / 24
            }
            if (id == "daysBtn") {
                days = Number(document.getElementById(`days`).value)
                document.getElementById(`minutes`).value = days * 1440
                document.getElementById(`hours`).value = days * 24
                document.getElementById(`seconds`).value = days * 86400
            }
        }
    }
}


function attachEventsListeners() {
    const dayRatios = {
        days: 1, hours: 24, minutes: 1440, seconds: 86400
    }

    function convert(value, unit) {
        const inDays = value / dayRatios[unit]
        return {
            days: inDays,
            hours: inDays * dayRatios.hours,
            minutes: inDays * dayRatios.minutes,
            seconds: inDays * dayRatios.seconds
        }
    }

    const daysInput = document.getElementById(`days`)
    const hoursInput = document.getElementById(`hours`)
    const minutesInput = document.getElementById(`minutes`)
    const secondsInput = document.getElementById(`seconds`)

    document.getElementById(`daysBtn`).addEventListener(`click`, onConvert)
    document.getElementById(`hoursBtn`).addEventListener(`click`, onConvert)
    document.getElementById(`minutesBtn`).addEventListener(`click`, onConvert)
    document.getElementById(`secondsBtn`).addEventListener(`click`, onConvert)


    function onConvert(ev) {
        const input = ev.target.parentElement.querySelector(`input[type="text"]`)
        const time = convert(Number(input.value), input.id)
        daysInput.value = time.days
        hoursInput.value = time.hours
        minutesInput.value = time.minutes
        secondsInput.value = time.seconds
    } 
}