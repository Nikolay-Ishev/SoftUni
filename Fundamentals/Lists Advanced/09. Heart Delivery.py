even_integer_list = input().split("@")
even_integer_list = [int(x) for x in even_integer_list]
command = input().split()
current_index = 0
while command[0] != 'Love!':
    current_house_index = current_index + int(command[1])
    current_index = current_house_index
    if current_house_index > len(even_integer_list) - 1:
        current_index = 0
        current_house_index = 0
    if even_integer_list[current_house_index] == 0:
        print(f"Place {current_house_index} already had Valentine's day.")
        command = input().split()
        continue
    even_integer_list[current_house_index] -= 2
    if even_integer_list[current_house_index] <= 0:
        even_integer_list[current_house_index] = 0
        print(f"Place {current_house_index} has Valentine's day.")
    command = input().split()
print(f"Cupid's last position was {current_index}.")
result = list(filter(lambda x: x != 0, even_integer_list))
if not result:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(result)} places.")
