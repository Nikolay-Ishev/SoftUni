n = int(input())
word = input()
full_list = []
word_list = []
for strings in range(n):
    current_word = input()
    full_list.append(current_word)
    if word in current_word:
        word_list.append(current_word)
print(full_list)
print(word_list)




