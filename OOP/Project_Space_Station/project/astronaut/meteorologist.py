from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        # some types of astronauts need more oxygen units while breathing.
        self.oxygen -= 15
