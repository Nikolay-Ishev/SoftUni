function filterEmp(data, criteria) {
    function represent(employer) {
        console.log(`${counter}. ${employer.first_name} ${employer.last_name} - ${employer.email}`)
        counter += 1
    }

    let counter = 0
    let employees = JSON.parse(data)
    if (criteria == `all`) {
        for (e of employees) {
            represent(e)
        }
    } else {
        [key, value] = criteria.split(`-`)
        for (e of employees) {
            if (e[key] == value) {
                represent(e)
            }
        }
    }
}







filterEmp(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`, 
  'gender-Female')