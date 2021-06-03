import re
counter = 1
with open("text.txt", "r") as file:
    for el in file.readlines():
        el = el.strip()
        punctuation_marks = len(re.findall(r"[^\w\s]", el))
        letters = len(re.findall(r"[a-zA-z]", el))
        el = f"Line {counter}: " + el + f" ({letters})({punctuation_marks})"
        print(el)
        counter += 1



