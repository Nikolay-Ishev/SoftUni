days = int(input())
hours_per_day = int(input())
total_sum = 0
for day in range(1, days + 1):
    day_sum = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_sum += 2.5
            day_sum += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_sum += 1.25
            day_sum += 1.25
        else:
            total_sum += 1
            day_sum += 1
    print(f"Day: {day} - {day_sum:.2f} leva")
print(f"Total: {total_sum:.2f} leva")


