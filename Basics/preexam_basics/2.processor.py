import math
processors_needed = int(input())
employees = int(input())
workdays = int(input())
hours = employees * workdays * 8
processors = math.floor(hours / 3)
if processors < processors_needed:
    looses = (processors_needed - processors) * 110.10
    print(f"Losses: -> {looses:.2f} BGN")
else:
    profit = (processors - processors_needed) * 110.10
    print(f"Profit: -> {profit:.2f} BGN")
