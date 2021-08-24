from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        # some types of astronauts need more oxygen units while breathing.
        self.oxygen -= 5


# test_bio = Biologist("t_name")
# print(test_bio.oxygen)
# test_bio.breathe()
# print(test_bio.oxygen)
