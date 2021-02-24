string = input()
word = ""
number = ""
number_end = False
final_string = ""
for i in range(len(string)):
    if not string[i].isdigit():
        word += string[i]
    else:
        number += string[i]
    if i == len(string) - 1:
        number_end = True
    elif not string[i + 1].isdigit() and string[i].isdigit():
        number_end = True
    if number_end:
        word = word.upper()
        number = int(number)
        final_string += word * number
        word = ""
        number = ""
        number_end = False
unique_set = ''.join(set(final_string))
print(f"Unique symbols used: {len(unique_set)}")
print(final_string)


"""ИЛИииииииииииииииииии
ИЛИиииииииииииииииииииии 
иииииииииииииииииииииИЛИ"""



string = input()
i = 0
word = ""
final_string = ""
while i < len(string):
    if not string[i].isdigit():
        word += string[i]
        i += 1
    else:
        number = ""
        while i < len(string) and string[i].isdigit():
            number += string[i]
            i += 1
        word = word.upper()
        number = int(number)
        final_string += word * number
        word = ""
unique_set = ''.join(set(final_string))
print(f"Unique symbols used: {len(unique_set)}")
print(final_string)



