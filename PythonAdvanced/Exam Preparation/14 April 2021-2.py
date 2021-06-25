def who_is_in_turn(p_1_turns, p_2_turns):
    if p_1_turns == p_2_turns:
        return "player_1"
    return "player_2"


def valid_coord_check(a, b):
    # row, col
    if 0 <= a < 7 and 0 <= b < 7:
        return True
    return False


player_1_name, player_2_name = input().split(", ")
dartboard = []
for rows in range(7):
    col = [x for x in input().split()]
    dartboard.append(col)
player_1_turns = 0
player_2_turns = 0
player_1_points = 501
player_2_points = 501

while player_1_points > 0 and player_2_points > 0:
    info = input().split(", ")
    row = int(info[0][1:])
    col = int(info[1][:-1])
    current_turn_score = 0
    player = who_is_in_turn(player_1_turns, player_2_turns)

    if player == "player_1":
        player_1_turns += 1
    else:
        player_2_turns += 1

    if not valid_coord_check(row, col):
        continue

    else:
        corresponding_numbers = int(dartboard[row][0]) + int(dartboard[row][6]) + int(dartboard[0][col]) + int(
            dartboard[6][col])
        if dartboard[row][col] == "B":
            current_turn_score = 501
        elif dartboard[row][col] == "T":
            current_turn_score = corresponding_numbers * 3
        elif dartboard[row][col] == "D":
            current_turn_score = corresponding_numbers * 2
        else:
            current_turn_score = int(dartboard[row][col])

        if player == "player_1":
            player_1_points -= current_turn_score
        else:
            player_2_points -= current_turn_score

if player_1_points <= 0:
    print(f"{player_1_name} won the game with {player_1_turns} throws!")
else:
    print(f"{player_2_name} won the game with {player_2_turns} throws!")
