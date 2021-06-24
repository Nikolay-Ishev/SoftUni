def stock_availability(*args):
    flavours_list = args[0]
    command = args[1]
    if command == "delivery":
        for i in range(2, len(args)):
            flavours_list.append(args[i])
    elif command == "sell":
        if len(args) > 2:
            if isinstance(args[2], int):
                flavours_list = flavours_list[args[2]:]
            else:
                for i in range(2, len(args)):
                    while args[i] in flavours_list:
                        flavours_list.remove(args[i])
        else:
            flavours_list = flavours_list[1:]
    return flavours_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))