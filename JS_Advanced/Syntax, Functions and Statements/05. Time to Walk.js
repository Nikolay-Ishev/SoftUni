function time_to_walk(steps, footprint_length, speed) {
    //Every 500 meters the student rests and takes a 1-minute break.
    
    distance_m = steps * footprint_length 
    speed_m_s = speed * 5/18
    brakes = Math.floor(distance_m / 500)
    totalSeconds = distance_m / speed_m_s + (brakes * 60)
    hours = Math.floor(totalSeconds / 3600);
    totalSeconds %= 3600;
    minutes = Math.floor(totalSeconds / 60);
    seconds = Math.round(totalSeconds % 60);

    function format_digit(digit) {
        let formattedDigit = digit.toLocaleString('en-US', {
            minimumIntegerDigits: 2,
            useGrouping: false })
        return formattedDigit
        }

    return `${format_digit(hours)}:${format_digit(minutes)}:${format_digit(seconds)}`
}

console.log(time_to_walk(4000, 0.60, 5))
