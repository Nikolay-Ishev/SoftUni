function createRecord(name, population, treasury) {
    const city = {};
    city.name = name;
    city.population = population;
    city.treasury = treasury;
    return city;

    //short sintax:
    
    // return {
    //     name,
    //     population,
    //     treasury
    //   };
    
  }
  