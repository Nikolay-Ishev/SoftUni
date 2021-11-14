function deleteByEmail() {
    //select input field and read value
    const input = document.querySelector(`input[name="email"]`);

    //get tbody children
    const rows = Array.from(document.querySelector(`tbody`).children);

    let removed = false

    //check for every row if textContent matches input value => remove row
    for (let row of rows) {
        if (row.children[1].textContent == input.value) {
            row.remove();
            removed = true;
        }
    }

    //print appropriate message depending from result
    if (removed) {
        document.getElementById(`result`).textContent = `Deleted.`;
    } else {
        document.getElementById(`result`).textContent = `Not found.`;
    }
}