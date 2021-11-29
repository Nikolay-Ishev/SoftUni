function notify(message) {
  function onClick(event) {
    notificationPanel.style.display = `none`
  }
  const notificationPanel = document.querySelector(`#notification`)
  notificationPanel.textContent = message
  notificationPanel.style.display = `block`
  notificationPanel.addEventListener(`click`, onClick)

}