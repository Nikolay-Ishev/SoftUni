function extractText() {
    const items = document.getElementById('items').children;
    const result = []

    for (const item of Array.from(items)) {
        result.push(item.textContent);
    }
    document.getElementById('result').textContent = result.join('\n')
}

function anotherExtractText() {
    let itemNodes = document.querySelectorAll("ul#items li");
    let textarea = document.querySelector("#result");
    for (let node of itemNodes) {
      textarea.value += node.textContent + "\n";
    }
  }
  