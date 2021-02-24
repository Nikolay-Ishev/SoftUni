import re

pattern = r"www\.[a-zA-Z0-9-]+(\.[a-z]+)+"
text = input()
links = []
while text:
    link = re.finditer(pattern, text)
    if link:
        for el in link:
            links.append(el.group())
    text = input()
[print(l) for l in links]
#(^|(?<=\s)) - започва в началото на реда или има спейс преди това
#($|(?=\s)) - завършва с него или има спейс отпред