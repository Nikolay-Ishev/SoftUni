function create(words) {
   let content = document.getElementById("content")
   for (let word of words) {
      let d = document.createElement("div");
      let p = document.createElement("p");
      p.textContent = word
      p.style.display = "none"
      d.appendChild(p)
      content.appendChild(d)
   }
   content.addEventListener(`click`, onClick)

   function onClick(ev) {
      let target = ev.target.childNodes[0]
      if (target.tagName == `P`) {
         target.style.display = 'block'
      }
   }
}