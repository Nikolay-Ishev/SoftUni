fire_list = [str(x) for x in input().split("#")]
water = int(input())
effort = 0
total_fire = 0
print("Cells:")
#RANGE_HIGH = range(81, 125 + 1)
#RANGE_MEDIUM = range(51, 80 +1)
#RANGE_LOW = range(1, 50 + 1)
#това са константи, които се пишат с главни букви и съдържат числа в някакви граници (последното +1)
#в условието долу се пише ------     if not fire_value in RANGE_***
for fire in fire_list:
    fire_type, fire_value = fire.split(" = ")
    fire_value = int(fire_value)
    if fire_type == "High" and not 81 <= fire_value <= 125:
        continue
    elif fire_type == "Medium" and not 51 <= fire_value <= 80:
        continue
    elif fire_type == "Low" and not 1 <= fire_value <= 50:
        continue
    if water < fire_value:
        continue
    water -= fire_value
    effort += 0.25 * fire_value
    total_fire += fire_value
    print(f" - {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
#ако не искам да започна с принт селс горе, а всички принтове да са заедно долу трябва да направя празен лист и докато
#цикълът върти да добавям стойностите в листа