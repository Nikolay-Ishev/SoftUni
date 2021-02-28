targets = input().split()
targets = [int(x) for x in targets]
shots = []
for i in range(len(targets)):
    shots.append(False)
command = input()
while command != "End":
    index = int(command)
    if 0 <= index < len(targets) and shots[index] is False:
        shots[index] = True
        for i in range(len(targets)):
            if shots[i] is True:
                continue
            if targets[i] > targets[index]:
                targets[i] -= targets[index]
            else:
                targets[i] += targets[index]
        targets[index] = -1
    command = input()
counter = 0
for e in shots:
    if e is True:
        counter += 1
string_targets = [str(n) for n in targets]
a = " ".join(string_targets)
print(f"Shot targets: {counter} -> {a}")


