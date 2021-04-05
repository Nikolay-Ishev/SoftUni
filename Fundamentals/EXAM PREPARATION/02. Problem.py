import re

n = int(input())
registrations = 0
pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"
for _ in range(n):
    data = input()
    match = re.findall(pattern, data)
    if match:
        registrations += 1
        print("Registration was successful")
        print(f"Username: {match[0][0]}, Password: {match[0][1]}")
    else:
        print("Invalid username or password")
print(f"Successful registrations: {registrations}")

