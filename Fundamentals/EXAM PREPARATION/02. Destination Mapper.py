import re

places = input()
pattern = r"(=|/)\b([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, places)
travel_points = 0
destinations = []
for match in matches:
    travel_points += len(match.group(2))
    destinations.append(match.group(2))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
