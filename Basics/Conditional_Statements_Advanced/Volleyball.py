import math
year = str(input())
holidays = int(input())
weekends_h = int(input())
#48 weekends total
# 48 - weekends_h = weekends_s
# 0.75 * weekends_s - почива
# 2/3 * holidays
volley = 0.75 * (48 - weekends_h) + 2/3 * holidays + weekends_h
if year == "normal":
    print(f"{math.floor(volley)}")
else:
    print(f"{math.floor(volley + (0.15 * volley))}")
