the_text = input()
for i in range(len(the_text)):
    if the_text[i] == ":":
        print(the_text[i] + the_text[i + 1])
