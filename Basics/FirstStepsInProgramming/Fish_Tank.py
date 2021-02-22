length = int(input())
width = int(input())
height = int(input())
occupied_volume = float(input())
full_volume = length * width * height

#L =cm³/1000.0

water_volume = ((100 - occupied_volume) / 100) * full_volume / 1000
print(water_volume)


