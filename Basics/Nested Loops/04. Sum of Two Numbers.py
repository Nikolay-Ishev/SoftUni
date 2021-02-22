first_number = int(input())
second_number = int(input())
magic_number = int(input())
combinations = 0
found = False
for a in range(first_number, second_number + 1):
    for b in range(first_number, second_number + 1):
        combinations += 1
        if a + b == magic_number:
            print(f"Combination N:{combinations} ({a} + {b} = {magic_number})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{combinations} combinations - neither equals {magic_number}")



