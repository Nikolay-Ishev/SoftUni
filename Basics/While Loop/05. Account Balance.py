unknown = input()
total = 0
while unknown != ("NoMoreMoney"):
    if float(unknown) < 0:
        print("Invalid operation!")
        break
    else:
        total += float(unknown)
        print (f"Increase: {float(unknown):.2f}")
        unknown = input()
print(f"Total: {total:.2f}")







