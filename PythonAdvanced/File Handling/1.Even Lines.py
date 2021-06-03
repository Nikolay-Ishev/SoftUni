import re

counter = 0
special_chars = "-,.!?"
with open("text.txt", "r") as file:
    for el in file.readlines():
        if counter % 2 == 0:
            el = re.sub("[-,.!?]", "@", el).strip()
            words = el.split(' ')
            reverse_sentence = ' '.join(reversed(words))
            print(reverse_sentence)
        counter += 1
