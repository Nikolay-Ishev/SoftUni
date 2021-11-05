function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);   
   function onClick() {
      const search = document.getElementById("searchField").value
      const rowArr = Array.from(document.querySelectorAll(`tbody tr`))
      for (let row of rowArr) {
         let match = false
         const elArr = Array.from(row.children)

         //textContent works directly on the row as well, no need for the second for cicle
         for (let el of elArr) {
            if (el.textContent .includes(search)) {
               match = true
               row.classList.add("select")
               break
            }
         }
         if (!match) {
            row.classList.remove("select")
         }
      }
   }
}