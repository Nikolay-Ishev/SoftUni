function colorize() {
    const rows = document.querySelectorAll(`table tr`)
    for (let i=1; i<rows.length ; i+=2) {
        rows[i].style.backgroundColor = `teal`;
    }
}

function colorize2() {
    const rows = document.querySelectorAll(`table tr:nth-child(even)`)
    for (el of rows) {
        el.style.backgroundColor = `teal`;
    }
}