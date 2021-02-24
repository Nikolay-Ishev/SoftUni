import re
phones = input()
pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
real_phones = re.finditer(pattern, phones)
#finditer дава iterable обект, по който можем да вървим с фор цикъл
real_phones = [p.group(0) for p in real_phones]
print(", ".join(real_phones))


