function day_of_week(day) {
    d_map = {
        'Monday': 1,
        'Tuesday': 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
   if (day in d_map) {
       console.log(d_map[day])
   } else console.log("error")
}

day_of_week('Monday')
day_of_week('Friday')
day_of_week('Sriada')