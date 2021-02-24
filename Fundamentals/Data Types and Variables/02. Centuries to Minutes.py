import math
centuries = int(input())
# centuries = 100 * years = 36524 days = 876576 hours = 52594560 minutes
years = centuries * 100
days = math.floor(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
