command = input()
courses = {}
while command != "end":
    name, student = command.split(" : ")
    if name not in courses:
        courses[name] = []
    courses[name].append(student)
    command = input()
ord_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for key, value in ord_courses.items():
    print(f"{key}: {len(value)}")
    for val in sorted(value):
        print(f"-- {val}")
