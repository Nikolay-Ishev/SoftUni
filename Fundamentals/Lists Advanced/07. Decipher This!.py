secret_message = input().split()
result = []
for word in secret_message:
    number = int(''.join([ele for ele in word if ele.isnumeric()]))
    char = chr(number)
    new_word = list(char + ''.join([ele for ele in word if not ele.isnumeric()]))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = ''.join(new_word)
    result.append(new_word)
print(' '.join(result))










