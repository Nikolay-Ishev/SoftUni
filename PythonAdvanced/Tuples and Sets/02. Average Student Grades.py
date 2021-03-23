n = int(input())
students = {}
for student in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = [float(grade)]
    else:
        students[name].append(float(grade))
for key, value in students.items():
    # grades = " ".join(f"{x:.2f}" for x in value)
    grades = " ".join(map(lambda x: f"{x:.2f}", value))
    print(f"{key} -> {grades} (avg: {sum(value) / len(value):.2f})")


