text = str(input())

# буква	    a	e	i	o	u
# стойност	1	2	3	4	5
final_sum = 0
for letter in text:
    if letter == "a":
        final_sum += 1
    elif letter == "e":
        final_sum += 2
    elif letter == "i":
        final_sum += 3
    elif letter == "o":
        final_sum += 4
    elif letter == "u":
        final_sum += 5
print(final_sum)

# for letter in range(0, len(text)):
#     if text[letter] == "a":
#         final_sum += 1
#     elif text[letter] == "e":
#         final_sum += 2
#     elif text[letter] == "i":
#         final_sum += 3
#     elif text[letter] == "o":
#         final_sum += 4
#     elif text[letter] == "u":
#         final_sum += 5
# print(final_sum)