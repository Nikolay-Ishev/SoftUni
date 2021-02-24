cards = input()
card_list = cards.split()
card_list = list(set(card_list))
team_a = 11
team_b = 11
for offs in range(len(card_list)):
    if card_list[offs][0] == "A":
        team_a -= 1
    else:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if team_a < 7 or team_b < 7:
    print("Game was terminated")
