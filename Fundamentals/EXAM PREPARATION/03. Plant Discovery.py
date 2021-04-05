# n = int(input())
# plants_rarities = {}
# plants_ratings = {}
# for _ in range(n):
#     plant, rarity = input().split("<->")
#     plants_rarities[plant] = rarity
# command = input()
# while command != "Exhibition":
#     command = command.split(": ")
#     try:
#         if command[0] == "Rate":
#             plant, rating = command[1].split(" - ")
#             if plant not in plants_ratings:
#                 plants_ratings[plant] = []
#             plants_ratings[plant].append(float(rating))
#         elif command[0] == "Update":
#             plant, new_rarity = command[1].split(" - ")
#             plants_rarities[plant] = new_rarity
#         elif command[0] == "Reset":
#             plant = command[1]
#             plants_ratings[plant].clear()
#             plants_ratings[plant].append(0)
#         else:
#             print("error")
#     except KeyError:
#         print("error")
#     command = input()
# plants = {}
# for key, value in plants_ratings.items():
#     avg_rating = sum(value) / len(value)
#     plants[key] = [plants_rarities[key], avg_rating]
# plants_ord = dict(sorted(plants.items(), key=lambda x: (-int(x[1][0]), -x[1][1])))
# print(f"Plants for the exhibition:")
# for key, value in plants_ord.items():
#     print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
# #
# #    50/100 judge with the code above


n = int(input())

plants = {}

for _ in range(n):
    plant_name, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant_name] = {'rarity': rarity, 'ratings': []}

data = input()

while not data == "Exhibition":
    command, command_params = data.split(": ")
    if command == "Rate":
        plant_name, rating = command_params.split(" - ")
        rating = int(rating)
        if plant_name in plants:
            plants[plant_name]['ratings'].append(rating)
        else:
            print("error")
    elif command == "Update":
        plant_name, rarity = command_params.split(" - ")
        rarity = int(rarity)
        if plant_name in plants:
            plants[plant_name]['rarity'] = rarity
        else:
            print("error")
    elif command == "Reset":
        plant_name = command_params
        if plant_name in plants:
            plants[plant_name]['ratings'].clear()
        else:
            print("error")
    else:
        print("error")
    data = input()


# Same while could be present more easily for errors like this:
# while not data == "Exhibition":
#     command, command_params = data.split(": ")
#     try:
#         if command == "Rate":
#             plant_name, rating = command_params.split(" - ")
#             rating = int(rating)
#             plants[plant_name]['ratings'].append(rating)
#         elif command == "Update":
#             plant_name, rarity = command_params.split(" - ")
#             rarity = int(rarity)
#             plants[plant_name]['rarity'] = rarity
#
#         elif command == "Reset":
#             plant_name = command_params
#             plants[plant_name]['ratings'].clear()
#
#         else:
#             print("error")
#     except KeyError:
#         print("error")
#     data = input()


for plant_name, value in plants.items():
    if value['ratings']:
        avg = sum(value['ratings']) / len(value['ratings'])
    else:
        avg = 0
    plants[plant_name]['avg'] = avg


# Please note that both options are valid because we must sort
# descenting INTEGER values (int values can be sorted desc with - infront of them)
sorted_plants = sorted(plants.items(), key=lambda tkvp: (-tkvp[1]['rarity'], -tkvp[1]['avg']))
# sorted_plants = sorted(plants.items(),  key=lambda tkvp: (tkvp[1]['rarity'], -tkvp[1]['avg']))

print("Plants for the exhibition:")
for plant_name, values in sorted_plants:
    print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: {values['avg']:.2f}")