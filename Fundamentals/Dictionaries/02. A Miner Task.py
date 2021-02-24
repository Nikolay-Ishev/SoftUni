command = input()
counter = 0
miner_dict = {}
while command != "stop":
    value = int(input())
    counter += 1
    if command not in miner_dict:
        miner_dict[command] = 0
    miner_dict[command] += value
    command = input()
for key, value in miner_dict.items():
    print(f"{key} -> {value}")

