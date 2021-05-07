def concatenate(*args):
    args_list = [x for x in args]
    return "".join(args_list)


print(concatenate("Soft", "Uni", "Is", "Great", "!"))