def numbers_searching(*args):
    from_smallest_to_biggest = True
    args_list = [int(x) for x in args]
    for i in range(len(args_list)):
        if args_list[i] == args[i+1]:
            continue
        if args[0] < args[i+1]:
            break
        elif args[0] > args[i+1]:
            from_smallest_to_biggest = False
            break
    sorted_list = sorted(set(args_list))
    if from_smallest_to_biggest:
        for i in range(len(sorted_list)-1):
            if sorted_list[i] + 1 != sorted_list[i + 1]:
                missing_number = sorted_list[i] + 1
    else:
        for i in range(len(sorted_list) - 1, 1, -1):
            if sorted_list[i] != sorted_list[i-1] + 1:
                missing_number = sorted_list[i] - 1

    duplicates = sorted(set([x for x in args_list if args_list.count(x) > 1]))
    return [missing_number, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))



