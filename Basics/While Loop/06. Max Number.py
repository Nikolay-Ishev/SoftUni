import sys
number = input()
biggest = -sys.maxsize
while number != "Stop":
    if biggest < float(number):
        biggest = int(number)
    number = input()
print(biggest)
