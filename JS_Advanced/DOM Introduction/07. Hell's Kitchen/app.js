function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
      let arr = JSON.parse(document.querySelector('#inputs textarea').value)
      const restaurants = []
      for (el of arr) {
         [restaurantName, workers] = el.split(` - `)
         workerArr = workers.split(`, `)
         alreadyExist = false
         let restaurant
         for (r of restaurants) {
            if (r.name == restaurantName) {
               restaurant = r
               for (w of workerArr) {
                  [wName, wSalary] = w.split(` `)
                  worker = { name: wName, salary: parseFloat(wSalary) }
                  restaurant.workers.push(worker)
                  restaurant.salariesTotal += worker.salary
                  if (worker.salary > restaurant.bestSalary) {
                     restaurant.bestSalary = worker.salary.toFixed(2)
                  }
               }
            }
         }
         if (!restaurant) {
            restaurant = {
               name: restaurantName,
               workers: [],
               salariesTotal: 0,
               avrgSalary: 0,
               inputOrder: 0,
               bestSalary: 0
            }
            for (w of workerArr) {
               [wName, wSalary] = w.split(` `)
               worker = { name: wName, salary: parseFloat(wSalary) }
               restaurant.workers.push(worker)
               restaurant.salariesTotal += worker.salary
               if (worker.salary > restaurant.bestSalary) {
                  restaurant.bestSalary = worker.salary.toFixed(2)
               }
            }
            restaurants.push(restaurant)
         }
      }
      for (let i = 0; i < restaurants.length; i++) {
         restaurants[i].avrgSalary = (restaurants[i].salariesTotal / restaurants[i].workers.length).toFixed(2)
         restaurants[i].inputOrder = i
      }

      restaurants.sort((a, b) => b.avrgSalary - a.avrgSalary || a.inputOrder - b.inputOrder);
      let bestRestaurant = restaurants[0];
      bestRestaurant.workers.sort((a, b) => b.salary - a.salary); 

      let workersArr = []
      for (w of bestRestaurant.workers) {
         workersArr.push(`Name: ${w.name} With Salary: ${w.salary}`)
      }

      let resultRestorant = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.avrgSalary} Best Salary: ${bestRestaurant.bestSalary}`
      let resultWorkers = workersArr.join(" ")
      document.querySelector('#bestRestaurant>p').textContent = resultRestorant;
      document.querySelector('#workers>p').textContent = resultWorkers;

   }
}