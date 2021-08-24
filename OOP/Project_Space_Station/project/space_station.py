from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        mapper = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."
        self.astronaut_repository.add(mapper[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."
        items_list = items.split(", ")
        self.planet_repository.add(Planet(name))
        for p in self.planet_repository.planets:
            if p.name == name:
                p.items = items_list
                return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(astronaut)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exists!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        current_planet = None
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                current_planet = planet
        if not current_planet:
            raise Exception("Invalid planet name!")

        # You should pick up to 5 astronauts with the highest amount of oxygen among the ones with oxygen above 30 un
        astronauts_oxygen_dict = {}
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                astronauts_oxygen_dict[astronaut] = astronaut.oxygen
        if not astronauts_oxygen_dict:
            raise Exception("You need at least one astronaut to explore the planet!")
        astronauts_oxygen_dict_sorted = dict(sorted(astronauts_oxygen_dict.items(), key=lambda x: -x[1]))
        astronauts_chosen = []
        for key, value in astronauts_oxygen_dict_sorted.items():
            astronauts_chosen.append(key)
            if len(astronauts_chosen) == 5:
                break
        # astronauts start going out in open space one by one, sorted in descending order by the amount of oxygen
        astro_number = 0
        for a in astronauts_chosen:
            if not current_planet.items:
                break
            astro_number += 1
            while True:
                if not current_planet.items:
                    break
                current_item = current_planet.items.pop()
                a.backpack.append(current_item)
                a.breathe()
                if a.oxygen <= 0:
                    break
        if current_planet.items:
            self.failed_missions += 1
            return "Mission is not completed."
        else:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {astro_number} astronauts participated in collecting items."

    def report(self):
        result = []
        result.append(f"{int(self.completed_missions)} successful missions!")
        result.append(f"{self.failed_missions} missions were not completed!")
        result.append("Astronauts' info:")
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                result.append(f"Backpack items: none")
        return "\n".join(result)

#
# space_test = SpaceStation()
# space_test.add_astronaut("Biologist", "1")
# space_test.add_astronaut("Biologist", "2")
# space_test.add_astronaut("Geodesist", "3")
# space_test.add_astronaut("Geodesist", "4")
# space_test.add_astronaut("Meteorologist", "5")
# space_test.add_astronaut("Meteorologist", "6")
# space_test.add_planet("test_planet", "item1, item2, item3, item4, item5, item6, item7")
# print(space_test.send_on_mission("test_planet"))




