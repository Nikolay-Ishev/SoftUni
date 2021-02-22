import math
video_price = int(input())
adapter_price = int(input())
electr_per_day = float(input())
income_per_day = float(input())
video = video_price * 13
adapter = adapter_price * 13
income = (income_per_day - electr_per_day) * 13
spend_money = video + adapter + 1000
days = spend_money / income
print(spend_money)
print(math.ceil(days))

