function addItem() {
    //select input field and read value
    let input = document.getElementById('newItemText');

    //create new <li> element
    let liElement = document.createElement("li");
    liElement.textContent = input.value;

    //create Delete button (anchor(hyperlink))
    const button = document.createElement(`a`);
    button.href = `#`;
    button.textContent = `[Delete]`;
    button.addEventListener(`click`, removeElement);

    //add the button to the DOM
    liElement.appendChild(button)

    //select <ul> and append new <li> element
    document.getElementById("items").appendChild(liElement);

      //clearing the input:
    input.value = '';

    function removeElement(ev) {
        const parent = ev.target.parentNode;
        parent.remove();
    }
  } 

