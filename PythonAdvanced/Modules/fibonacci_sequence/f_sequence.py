def locate_sequence(x):
    a = 0
    b = 1
    f_list = [a]
    while int(x) > f_list[-1]:
        f_list.append(b)
        b = f_list[-1] + f_list[-2]
    if int(x) == f_list[-1]:
        print(f"The number - {x} is at index {len(f_list) - 1}")
    else:
        print(f"The number {x} is not in the sequence")


def create_sequence(x):
    a = 0
    b = 1
    f_list = [a]
    while int(x) > len(f_list):
        f_list.append(b)
        b = f_list[-1] + f_list[-2]
    print(*f_list)


def fibonacci_sequence(args_list):
    if args_list[0] == "Create":
        create_sequence(int(args_list[2]))
    elif args_list[0] == "Locate":
        locate_sequence(args_list[1])

