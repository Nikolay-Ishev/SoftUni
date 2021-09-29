function road_radar(current_speed, area) {
    max_speed_mapper = {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    }

    if (max_speed_mapper[area] >= current_speed) {
        return `Driving ${current_speed} km/h in a ${max_speed_mapper[area]} zone`
    }
    let over_speed = current_speed - max_speed_mapper[area]
    function status(over_speed) {
        if (over_speed <= 20) {
            return "speeding"
        }
        else if (over_speed <= 40) {
            return "excessive speeding"
        }
        else return "reckless driving"
    }
    return `The speed is ${over_speed} km/h faster than the allowed speed of ${max_speed_mapper[area]} - ${status(over_speed)}`
}

console.log(road_radar(21, 'residential'))