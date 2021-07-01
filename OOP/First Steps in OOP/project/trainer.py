from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name, pokemons=[]):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                found = True
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        info = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            details = p.pokemon_details()
            if p == self.pokemons[-1]:
                info += f"- {details}"
            else:
                info += f"- {details}\n"
        return info



