import re


def replace(st):
    st = re.sub(r'(.)\1+', r'\1', st)
    return st


# Driver code
string = input()
print(replace(string))
