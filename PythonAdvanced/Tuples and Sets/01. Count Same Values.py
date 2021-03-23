numbers_tuple = (float(x) for x in input().split())
num_occurrences = {}
for n in numbers_tuple:
    if n not in num_occurrences:
        num_occurrences[n] = 0
    num_occurrences[n] += 1

[print(f"{key} - {value} times") for key, value in num_occurrences.items()]

