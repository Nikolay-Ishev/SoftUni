##Shadowmourne – requires 250 Shards
# Valanyr – requires 250 Fragments
# Dragonwrath – requires 250 Motes
key_math_dict = {"fragments": 0, "shards": 0, "motes": 0}
junk_dict = {}
legendary_item = False
dropped_item = None
while not legendary_item:
    materials = input().split()
    materials = [x.lower() for x in materials]
    for i in range(1, len(materials) + 1, 2):
        if materials[i] == 'fragments' or materials[i] == 'shards' or materials[i] == 'motes':
            key_math_dict[materials[i]] += int(materials[i - 1])
            if key_math_dict[materials[i]] >= 250:
                legendary_item = True
                key_math_dict[materials[i]] -= 250
                if materials[i] == "shards":
                    dropped_item = "Shadowmourne"
                elif materials[i] == "fragments":
                    dropped_item = "Valanyr"
                else:
                    dropped_item = "Dragonwrath"
                break
        else:
            if materials[i] not in junk_dict:
                junk_dict[materials[i]] = 0
            junk_dict[materials[i]] += int(materials[i - 1])
print(f"{dropped_item} obtained!")

sorted_key = dict(sorted(key_math_dict.items(), key=lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(junk_dict.items(), key=lambda x: x[0]))
for key, value in sorted_key.items():
    print(f"{key}: {value}")
for key, value in sorted_junk.items():
    print(f"{key}: {value}")
