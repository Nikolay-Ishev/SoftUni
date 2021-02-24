# import re
import string

allowed_chars = string.ascii_letters + string.digits + '_-'
user_n = input().split(", ")
# for el in user_n:
#     if re.match("^[A-Za-z0-9_-]*$", el) and 2 < len(el) < 17:
#         print(el)

for word in user_n:
    check = True
    for el in word:
        if el not in allowed_chars:
            check = False
            break
    if check and 2 < len(word) < 17:
        print(word)
