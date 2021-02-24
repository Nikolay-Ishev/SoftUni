snowballs = int(input())
best_value = 0
best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0

for data in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_snow / snowball_time) ** snowball_quality
    if value > best_value:
        best_value = value
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
print(f"{best_snowball_snow} : {best_snowball_time} = {int(best_value)} ({best_snowball_quality})")
