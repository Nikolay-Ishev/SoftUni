def valid_coord_check(a, b):
    # row, col
    if 0 <= a < 5 and 0 <= b < 5:
        return True
    return False


moves_dict = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

matrix = []
hit_targets = []
for _ in range(5):
    row = [x for x in input().split()]
    matrix.append(row)

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            player_position = (row, col)

left_targets = 0
for row in matrix:
    left_targets += row.count("x")

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "shoot":
        target_row = player_position[0] + moves_dict[direction][0]
        target_col = player_position[1] + moves_dict[direction][1]
        while True:
            if not valid_coord_check(target_row, target_col):
                break
            if matrix[target_row][target_col] == "x":
                hit_targets.append([target_row, target_col])
                matrix[target_row][target_col] = "."
                left_targets -= 1
                break
            target_row += moves_dict[direction][0]
            target_col += moves_dict[direction][1]
    elif action == "move":
        steps = int(command[2])
        move_row = player_position[0] + moves_dict[direction][0] * steps
        move_col = player_position[1] + moves_dict[direction][1] * steps
        if valid_coord_check(move_row, move_col):
            if matrix[move_row][move_col] == ".":
                matrix[player_position[0]][player_position[1]] = "."
                matrix[move_row][move_col] = "A"
                player_position = (move_row, move_col)
    if not left_targets:
        print(f"Training completed! All {len(hit_targets)} targets hit.")
        break
if left_targets:
    print(f"Training not completed! {left_targets} targets left.")
for pos in hit_targets:
    print(pos)