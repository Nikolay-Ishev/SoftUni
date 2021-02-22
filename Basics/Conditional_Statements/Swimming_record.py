import math
record_s = float(input())
distance_m = float(input())
time_per_meter_s = float(input())
time = distance_m * time_per_meter_s
slowing = math.floor(distance_m / 15) * 12.5
# math.floor(distance_m / 15) е същото като (distance_m // 15)
real_time = time + slowing
if real_time < record_s:
    print(f"Yes, he succeeded! The new world record is {real_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(real_time - record_s):.2f} seconds slower.")

