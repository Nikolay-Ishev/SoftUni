from collections import deque


def remove_materials(f_list, expl_list):
    f_list.popleft()
    expl_list.pop()
    return f_list, expl_list


fireworks = deque([int(x) for x in input().split(", ")])
explosives = [int(x) for x in input().split(", ")]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
perfect_show = False

while len(fireworks) > 0 and len(explosives) > 0:
    if perfect_show:
        break
    current_firework = fireworks[0]
    current_explosive = explosives[-1]
    if current_firework <= 0:
        fireworks.popleft()
        continue
    if current_explosive <= 0:
        explosives.pop()
        continue
    mix = current_explosive + current_firework
    if mix % 3 == 0 and mix % 5 == 0:
        fireworks, explosives = remove_materials(fireworks, explosives)
        crossette_fireworks += 1
    elif mix % 3 == 0:
        fireworks, explosives = remove_materials(fireworks, explosives)
        palm_fireworks += 1
    elif mix % 5 == 0:
        fireworks, explosives = remove_materials(fireworks, explosives)
        willow_fireworks += 1
    else:
        fireworks[0] -= 1
        fireworks.append(fireworks.popleft())
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        perfect_show = True

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosives:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosives])}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
