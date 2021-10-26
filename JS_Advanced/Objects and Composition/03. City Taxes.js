function cityTaxes(name, population, treasury) {
    const city = {};
    city.name = name;
    city.population = population;
    city.treasury = treasury;
    city.taxRate = 10
    city.collectTaxes = function () {
        city.treasury += Math.floor(city.population * city.taxRate)
    }
    city.applyGrowth = function (percentage) {
        city.population += Math.floor(city.population * percentage / 100)
    }
    city.applyRecession = function (percentage) {
        city.treasury -= Math.ceil(city.treasury * percentage / 100)
    }
    return city;
}

function taxes(name, population, treasury) {
    return {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += Math.floor(this.population * this.taxRate)
        },
        applyGrowth(percentage) {
            this.population += Math.floor(this.population * percentage / 100)
        },
        applyRecession(percentage) {
            this.treasury -= Math.ceil(this.treasury * percentage / 100)
        }
    }
}

let city =
taxes('Tortuga',
        7000,
        15000);
console.log(city);

city =
taxes('Tortuga',
        7000,
        15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);

