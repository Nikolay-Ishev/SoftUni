def best_list_pureness(numbers, rotations):
    pureness = {}
    for r in range(rotations + 1):
        current_pureness = 0
        for i in range(len(numbers)):
            current_pureness += int(numbers[i]) * i
        pureness[r] = current_pureness
        numbers = numbers[-1:] + numbers[:-1]
    sorted_pureness = dict(sorted(pureness.items(), key=lambda x: (-x[1], x[0])))
    # for key, value in sorted_pureness.items():
    #     print(key, value)
    rotations, best_pureness = (next(iter(sorted_pureness.items())))
    current_result = f"Best pureness {best_pureness} after {rotations} rotations"
    return current_result


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)