text = input()
encrypt = [chr((ord(a) + 3)) for a in text]
# encrypt = map(lambda a: chr((ord(a) + 3)), text)
print("".join(encrypt))


