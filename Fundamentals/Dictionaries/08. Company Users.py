command = input()
companies = {}
while command != "End":
    key, value = command.split(' -> ')
    if key not in companies:
        companies[key] = []
    if value not in companies[key]:
        companies[key].append(value)
    command = input()
companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for key, value in companies.items():
    print(f"{key}")
    for v in value:
        print(f"-- {v}")
