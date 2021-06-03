# with open("text.txt", "w") as file:
#     file.write("This is some random line\nThis is the second line\nAnd this is the third one")
try:
    with open("text.txt", "r") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")
