input_string = input()
input_multiplier = int((input()))


def string_multiply(string, multiplier):
    result = int(multiplier) * str(string)
    return result


print(string_multiply(input_string, input_multiplier))

#в презентацията е дадено с фор цикъл и += към резултата при всяка интерация
