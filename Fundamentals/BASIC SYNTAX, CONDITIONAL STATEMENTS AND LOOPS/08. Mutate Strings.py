string_1 = input()
string_2 = input()

result_compare = string_1
# print(string_1[0])
# print(string_1[1])
for iteration in range(0, len(string_1)):
    result_string = ""
    for index_str_2 in range(0, iteration +1):
        result_string += string_2[index_str_2]
    for index_str_1 in range(iteration + 1, len(string_1)):
        result_string += string_1[index_str_1]
    if result_string != result_compare:
        print(result_string)
        result_compare = result_string




