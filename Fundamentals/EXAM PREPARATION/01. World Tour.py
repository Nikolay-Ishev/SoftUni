tour = input()
command = input()
while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if 0 <= index < len(tour):
            tour = tour[:index] + string + tour[index:]
        print(tour)
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(tour) and 0 <= end_index < len(tour):
            tour = tour[:start_index] + tour[1 + end_index:]
        print(tour)
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in tour:
            tour = tour.replace(old_string, new_string)
        print(tour)
    command = input()
print(f"Ready for world tour! Planned stops: {tour}")


