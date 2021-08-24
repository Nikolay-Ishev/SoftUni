class PlanetRepository:
    def __init__(self):
        self.planets = []

    # planet: Planet
    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet
