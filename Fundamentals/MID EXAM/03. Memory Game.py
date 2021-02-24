el_list = input().split()
command = input()
moves = 0
win = False
while command != 'end':
    moves += 1
    command = [int(x) for x in command.split()]
    if command[0] == command[1] or not 0 <= command[0] <= len(el_list) - 1 or not 0 <= command[1] <= len(el_list) - 1:
        midpoint = len(el_list) // 2  # for 7 items, after the 3th
        el_list = el_list[0:midpoint] + 2 * [f"-{moves}a"] + el_list[midpoint:]
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if el_list[command[0]] == el_list[command[1]]:
        match_el = el_list[command[0]]
        print(f"Congrats! You have found matching elements - {match_el}!")
        el_list = [e for e in el_list if e != match_el]
    elif el_list[command[0]] != el_list[command[1]]:
        print(f"Try again!")
    if len(el_list) == 0:
        win = True
        break
    command = input()
if win:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(el_list))
