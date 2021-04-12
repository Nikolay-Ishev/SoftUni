countries = input().split(", ")
capitals = input().split(", ")
countries_dict = {countries[i]: capitals[i] for i in range(len(countries))}
[print(f"{key} -> {value}") for key, value in countries_dict.items()]
