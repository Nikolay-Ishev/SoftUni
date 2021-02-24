import re

text = input()
word = input()
pattern = f"(?i)\\b{word}\\b"
matches = re.findall(pattern, text)
print(len(matches))
