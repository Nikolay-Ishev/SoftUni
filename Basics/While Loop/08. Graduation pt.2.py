name = input()
year = 1
average = 0
while year <= 12:
    grade = float(input())
    if grade >= 4:
        year += 1
        average += grade
    else:
        grade = float(input())
        if grade >= 4:
            year += 1
            average += grade
        else:
            print(f"{name} has been excluded at {year} grade")
            break
if year >= 12:
    print(f"{name} graduated. Average grade: {(average / 12):.2f}")


