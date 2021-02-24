def jump(length):
    if position + length <= len(neighborhood) - 1:
        house_index = position + length
    else:
        house_index = 0

    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] <= 0:
            neighborhood[house_index] = 0
            print(f"Place {house_index} has Valentine's day.")
    return house_index


success = False
position = 0
neighborhood_command = input().split('@')
neighborhood = [int(x) for x in neighborhood_command]
#горните 2 реда могат да се обединят -  neighborhood = [int(x) for x in input().split('@']
command = input()
while command != "Love!":
    command = command.split()
    position = jump(int(command[1]))
    command = input()
if neighborhood.count(0) == len(neighborhood):
    success = True
print(f"Cupid's last position was {position}.")
if success:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")
