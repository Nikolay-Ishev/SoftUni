function createAssemblyLine() {
    return {
        hasClima: function(obj) {
            obj.temp = 21
            obj.tempSettings = 21
            obj.adjustTemp = function() {
                if (obj.temp < obj.tempSettings) {
                    obj.temp += 1
                }
                else if (obj.temp > obj.tempSettings) {
                    obj.temp -= 1
                }
                return
            }
        },
        hasAudio: function(obj) {
            obj.currentTrack = {
                name: null,
                artist: null,
            }
            obj.nowPlaying = function() {
                if (obj.currentTrack.name == null || obj.currentTrack.artist == null) {return}
                console.log(`Now playing '${obj.currentTrack.name}' by ${obj.currentTrack.artist}`)
                return
            }
        },
        hasParktronic: function(obj) {
            obj.checkDistance = function(distance) {
                if (distance<0.1) {
                    console.log("Beep! Beep! Beep!")
                    return
                }if (distance<0.25) {
                    console.log("Beep! Beep!")
                    return
                }if (distance<0.5) {
                    console.log("Beep!")
                    return
                } else {console.log("")}
                return
            }
        }
    }
}

const assemblyLine = createAssemblyLine();

const myCar = {
    make: 'Toyota',
    model: 'Avensis'
};

assemblyLine.hasClima(myCar);
console.log(myCar.temp);
myCar.tempSettings = 18;
myCar.adjustTemp();
console.log(myCar.temp);
assemblyLine.hasAudio(myCar);
myCar.currentTrack = {
    name: 'Never Gonna Give You Up',
    artist: 'Rick Astley'
};
myCar.nowPlaying();
assemblyLine.hasParktronic(myCar);
myCar.checkDistance(0.4);
myCar.checkDistance(0.2);
console.log(myCar);