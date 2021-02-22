hours = int(input())
minutes = int(input())
minutes_result = minutes + 15
if 10 <= minutes_result <= 59:
    print(f"{hours}:{minutes_result}")
elif minutes_result < 10:
    print(f"{hours}:0{minutes_result}")
else:
    new_minutes = minutes_result - 60
    hours += 1
    if new_minutes < 10:
        if hours <= 23:
            print(f"{hours}:0{new_minutes}")
        else:
            new_hours = hours - 24
            print(f"{new_hours}:0{new_minutes}")
    else:
        if hours <= 23:
            print(f"{hours}:{new_minutes}")
        else:
            new_hours = hours - 24
            print(f"{new_hours}:{new_minutes}")
