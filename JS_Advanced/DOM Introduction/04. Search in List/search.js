function search() {
   const towns = Array.from(document.querySelectorAll(`#towns li`))
   let search = document.getElementById("searchText").value
   let matches = 0
   for (let town of towns) {
      if (town.textContent.includes(search)) {
         town.style.textDecoration = `underline`
         town.style.fontWeight="bold"
         matches += 1
      }
      else {
         town.style.textDecoration = ``
         town.style.fontWeight= ``
      }
   }
   document.getElementById(`result`).textContent = `${matches} matches found`
}
