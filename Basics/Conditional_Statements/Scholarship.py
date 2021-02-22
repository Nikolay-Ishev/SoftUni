import math
income = float(input())
grades = float(input())
min_salary = float(input())
if grades <= 4.5:
    print("You cannot get a scholarship!")
elif grades < 5.5:
    if income >= min_salary:
        print("You cannot get a scholarship!")
    else:
        social_scholarship = 0.35 * min_salary
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
else:
    if income >= min_salary:
        scholarship = 25 * grades
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
    else:
        social_scholarship = 0.35 * min_salary
        scholarship = 25 * grades
        if social_scholarship > scholarship:
            print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
        else:
            print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")

