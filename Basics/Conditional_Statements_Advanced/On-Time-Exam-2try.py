h_beginning = int(input())
m_beginning = int(input())
h_arrival = int(input())
m_arrival = int(input())
arrival_time = (60 * h_arrival) + m_arrival
beginning_time = (60 * h_beginning) + m_beginning
time_difference = beginning_time - arrival_time
if -60 < time_difference < 0:
    print("Late")
    print(f"{time_difference * -1} minutes after the start")
elif -60 >= time_difference:
    print("Late")
    if (abs(time_difference) % 60) >= 10:
        print(f"{abs(time_difference) // 60}:{abs(time_difference) % 60} hours after the start")
    else:
        print(f"{abs(time_difference) // 60}:0{abs(time_difference) % 60} hours after the start")
elif 0 <= time_difference <= 30:
    print("On time")
    if time_difference > 0:
        print(f"{time_difference} minutes before the start")
else:
    print("Early")
    if time_difference < 60:
        print(f"{time_difference} minutes before the start")
    else:
        if (time_difference % 60) >= 10:
            print(f"{time_difference // 60}:{time_difference % 60} hours before the start")
        else:
            print(f"{time_difference // 60}:0{time_difference % 60} hours before the start")
        # :02d - формат, който слага 0 пред едноцифреното число


