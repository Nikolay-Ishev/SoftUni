steps = 0
while steps < 10000:
    command = input()
    if command == "Going home":
        command = int(input())
        steps += command
        break
    else:
        steps += int(command)
if steps < 10000:
    print(f"{10000 - steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps - 10000} steps over the goal!")
