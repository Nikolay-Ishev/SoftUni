favourite = input()
book = input()
number = 0
while book != favourite:
    if book == ("No More Books"):
        print("The book you search is not here!")
        print(f"You checked {number} books.")
        break
    else:
        number += 1
        book = input()
if book == favourite:
    print(f"You checked {number} books and found it.")







