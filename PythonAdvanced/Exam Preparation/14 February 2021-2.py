from math import floor


def valid_coord_check(a, b, n):
    # row, col, board_size
    if 0 <= a < n and 0 <= b < n:
        return True
    return False


def not_a_wall(a, b, n):
    # row, col, field
    if n[a][b] == "X":
        return False
    return True


moves_dict = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

size = int(input())
field = []
# create field
for _ in range(size):
    row = [x for x in input().split()]
    field.append(row)

# find player position
player_positions = []
for row in range(size):
    for col in range(size):
        if field[row][col] == "P":
            position = [row, col]
            player_positions.append(position)

coins = 0
command = input()
loose = False

while coins < 100:
    if command not in moves_dict:
        command = input()
        continue
    current_position_row = player_positions[-1][0]
    current_position_col = player_positions[-1][1]
    move_row = current_position_row + moves_dict[command][0]
    move_col = current_position_col + moves_dict[command][1]
    if valid_coord_check(move_row, move_col, size) and not_a_wall(move_row, move_col, field):
        coins += int(field[move_row][move_col])
        field[move_row][move_col] = 0
        new_position = [move_row, move_col]
        player_positions.append(new_position)
        if coins >= 100:
            break
    else:
        coins = coins / 2
        loose = True
        break
    command = input()

total_coins = floor(coins)
if not loose:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print("Your path:")
for i in range(1, len(player_positions)):
    print(player_positions[i])
