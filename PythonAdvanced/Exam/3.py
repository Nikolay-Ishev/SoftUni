def math_operations(*args, **kwargs):
    counter = 1
    args_list = [int(x) for x in args]
    while args_list:
        if counter == 5:
            counter = 1
        if counter == 1:
            kwargs["a"] = kwargs["a"] + args_list[0]
        elif counter == 2:
            kwargs["s"] = kwargs["s"] - args_list[0]
        elif counter == 3:
            if args_list[0] == 0:
                del args_list[0]
                counter += 1
                continue
            kwargs["d"] = kwargs["d"] / args_list[0]
        elif counter == 4:
            kwargs["m"] = kwargs["m"] * args_list[0]
        del args_list[0]
        counter += 1
    return kwargs



print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
