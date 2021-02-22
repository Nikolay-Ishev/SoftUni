h_beginning = int(input())
m_beginning = int(input())
h_arrival = int(input())
m_arrival = int(input())
if h_beginning == h_arrival:
    if m_beginning == m_arrival:
        print("On time")
    elif m_beginning > m_arrival and (m_beginning - m_arrival) <= 30:
        print("On time")
        print(f"{m_beginning - m_arrival} minutes before the start")
    elif m_beginning > m_arrival:
        print("Early")
        print(f"{m_beginning - m_arrival} minutes before the start")
    elif m_beginning < m_arrival:
        print("Late")
        print(f"{m_arrival - m_beginning} minutes after the start")
elif h_beginning < h_arrival:
    print("Late")
    if h_arrival - h_beginning == 1 and (60 - m_beginning + m_arrival) < 60:
        print(f"{60 - m_beginning + m_arrival} minutes after the start")
    else:
        if m_beginning > m_arrival:
            if (60 - m_beginning + m_arrival) >= 10:
                print(f"{h_arrival - h_beginning - 1}:{60 - m_beginning + m_arrival} hours after the start")
            else:
                print(f"{h_arrival - h_beginning - 1}:0{60 - m_beginning + m_arrival} hours after the start")
        else:
            if (m_arrival - m_beginning) >= 10:
                print(f"{h_arrival - h_beginning}:{m_arrival - m_beginning} hours after the start")
            else:
                print(f"{h_arrival - h_beginning}:0{m_arrival - m_beginning} hours after the start")
else:

    if h_beginning - h_arrival == 1 and (60 - m_arrival + m_beginning) <= 30:
        print("On time")
        print(f"{60 - m_arrival + m_beginning} minutes before the start")
    elif h_beginning - h_arrival == 1 and (60 - m_arrival + m_beginning) < 60:
        print("Early")
        print(f"{60 - m_arrival + m_beginning} minutes before the start")
    else:
        print("Early")
        if m_beginning == m_arrival:
            print(f"{h_beginning - h_arrival}:0{m_beginning - m_arrival} hours before the start")
        elif (60 - m_arrival + m_beginning) < 60:
            print(f"{h_beginning - h_arrival - 1}:{60 - m_arrival + m_beginning} hours before the start")
        else:
            if m_beginning - m_arrival >= 10:
                print(f"{h_beginning - h_arrival}:{m_beginning - m_arrival} hours before the start")
            else:
                print(f"{h_beginning - h_arrival}:0{m_beginning - m_arrival} hours before the start")








