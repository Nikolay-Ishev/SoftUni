function addItem() {
    const text = document.getElementById(`newItemText`)
    const value = document.getElementById(`newItemValue`)
    const opt = document.createElement('option');
    const menu = document.getElementById(`menu`)
    opt.textContent = text.value
    opt.value = value.value
    menu.appendChild(opt)
    text.value = ""
    value.value= ""
}