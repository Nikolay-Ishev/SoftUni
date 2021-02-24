command = input()
force = {}
while command != "Lumpawaroo":
    command_list = command.split()
    if "|" in command_list:
        command_list = command.split(' | ')
        key = command_list[0]
        value = command_list[1]
        check = False
        for keys, values in force.items():
            if value in values:
                check = True
                break
        if not check:
            if key not in force:
                force[key] = []
            force[key].append(value)
    else:
        command_list = command.split(' -> ')
        key = command_list[1]
        value = command_list[0]
        if key not in force:
            force[key] = []
        for side in force:
            if side == key:
                if value not in force[key]:
                    force[key].append(value)
                print(f"{value} joins the {key} side!")
            else:
                while value in force[side]:
                    force[side].remove(value)
    command = input()
force_sorted = dict(sorted(force.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in force_sorted.items():
    if len(value) == 0:
        continue
    else:
        print(f'Side: {key}, Members: {len(value)}')
        for v in sorted(value):
            print(f'! {v}')
