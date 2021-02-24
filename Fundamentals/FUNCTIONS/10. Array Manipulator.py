def exchange(element, index):
    if index > len(element) - 1 or index < 0:
        print("Invalid index")
        return element
    else:
        first_part = element[:index + 1]
        second_part = element[index + 1:]
        return second_part + first_part


def max_even(element):
    no_matches = True
    for i in element:
        if i % 2 == 0:
            no_matches = False
            break
        else:
            continue
    if no_matches:
        return "No matches"
    m = max(i for i in element if i % 2 == 0)  # намира най-големият четен елемент
    p = [i for i, j in enumerate(element) if j == m]  # намира всички индекси на най-г четен елемент
    return max(p) # намира най-големия индекс


def max_odd(element):
    no_matches = True
    for i in element:
        if i % 2 != 0:
            no_matches = False
            break
        else:
            continue
    if no_matches:
        return "No matches"
    m = max(i for i in element if i % 2 != 0)   #намира най-големият нечетен елемент
    p = [i for i, j in enumerate(element) if j == m]  #намира най-големият индекс на нечетния елемент
    return max(p)


def min_odd(element):
    no_matches = True
    for i in element:
        if int(i) % 2 != 0:
            no_matches = False
            break
        else:
            continue
    if no_matches:
        return "No matches"
    m = min(i for i in element if i % 2 != 0)   #намира най-малкия нечетен елемент
    p = [i for i, j in enumerate(element) if j == m]  #намира най-големият индекс на нечетния елемент
    return max(p)


def min_even(element):
    no_matches = True
    for i in element:
        if int(i) % 2 == 0:
            no_matches = False
            break
        else:
            continue
    if no_matches:
        return "No matches"
    m = min(i for i in element if i % 2 == 0)   #намира най-малкия четен елемент
    p = [i for i, j in enumerate(element) if j == m]  #намира най-големият индекс на четния елемент
    return max(p)


def first_even(element, count):
    new_list = []
    count = int(count)
    if int(count) > len(element) or int(count) <= 0:
        return 'Invalid count'
    for i in range(0, len(element)):
        if element[i] % 2 == 0:
            new_list.append(element[i])
            count -= 1
            if count == 0:
                return new_list
    return new_list


def first_odd(element, count):
    new_list = []
    count = int(count)
    if int(count) > len(element) or int(count) <= 0:
        return 'Invalid count'
    for i in range(0, len(element)):
        element[i] = int(element[i])
    for i in range(0, len(element)):
        if element[i] % 2 != 0:
            new_list.append(element[i])
            count -= 1
            if count == 0:
                return new_list
    return new_list


def last_odd(element, count):
    new_list = []
    count = int(count)
    if int(count) > len(element) or int(count) <= 0:
        return 'Invalid count'
    for i in range(len(element) - 1, - 1, -1):
        if element[i] % 2 != 0:
            new_list.append(element[i])
            count -= 1
            if count == 0:
                return new_list[::-1]
    return new_list[::-1]


def last_even(element, count):
    new_list = []
    count = int(count)
    if int(count) > len(element) or int(count) <= 0:
        return 'Invalid count'
    for i in range(len(element) - 1, - 1, -1):
        if element[i] % 2 == 0:
            new_list.append(element[i])
            count -= 1
            if count == 0:
                return new_list[::-1]
    return new_list[::-1]


int_list = input().split()
int_list = [int(x) for x in int_list]
# може да се използва map, след което обектът map да се преобразува отново в в лист
# int_list = list(map(int, int_list))
# map(в какво да преобразува, кое да преобразува)

command = input().split()
while command[0] != "end":
    if command[0] == "exchange":
        int_list = exchange(int_list, int(command[1]))
    elif command[0] == "max" and command[1] == "even":
        print(max_even(int_list))
    elif command[0] == "max" and command[1] == "odd":
        print(max_odd(int_list))
    elif command[0] == "min" and command[1] == "even":
        print(min_even(int_list))
    elif command[0] == "min" and command[1] == "odd":
        print(min_odd(int_list))
    elif command[0] == "first" and command[2] == "even":
        print(first_even(int_list, command[1]))
    elif command[0] == "first" and command[2] == "odd":
        print(first_odd(int_list, command[1]))
    elif command[0] == "last" and command[2] == "odd":
        print(last_odd(int_list, command[1]))
    elif command[0] == "last" and command[2] == "even":
        print(last_even(int_list, command[1]))
    command = input().split()
print(int_list)







