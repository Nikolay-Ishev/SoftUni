string = input()
dictionary = {}
for element in string:
    if element == " ":
        continue
    elif element not in dictionary:
        dictionary[element] = 0
    dictionary[element] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")
