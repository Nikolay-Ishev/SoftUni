import sys
number = input()
smallest = sys.maxsize
while number != "Stop":
    if smallest > int(number):
        smallest = int(number)
    number = input()
print(smallest)
