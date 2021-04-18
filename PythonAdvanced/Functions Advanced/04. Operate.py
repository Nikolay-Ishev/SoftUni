from functools import reduce


# eval превръща стринг в код, но не е препоръчително да се ползва, защото може да се манипулира лесно
def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


# по-правилното решение в случая е с if на всеки оператор или още по-добре - да се извадят ламбдите в дикшънари

print(operate("+", 1, 2, 3))
