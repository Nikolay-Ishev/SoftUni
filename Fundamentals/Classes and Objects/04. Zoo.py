class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            names = ', '.join(self.mammals)
            species_title = 'Mammals'
        elif species == 'fish':
            names = ', '.join(self.fish)
            species_title = 'Fishes'
        elif species == 'bird':
            names = ', '.join(self.birds)
            species_title = 'Birds'
        return f"{species_title} in {self.name}: {names}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for animal_info in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))


