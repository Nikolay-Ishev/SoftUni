days = int(input())
room = str(input())
feedback = str(input())
price = 0
if room == "room for one person":
    price += 18
    sum1 = price * (days - 1)
    if feedback == "positive":
        final_sum = sum1 + (0.25 * sum1)
        print(f"{final_sum:.2f}")
    elif feedback == "negative":
        final_sum = sum1 - (0.1 * sum1)
        print(f"{final_sum:.2f}")
elif room == "apartment":
    price += 25
    sum2 = price * (days - 1)
    if days < 10:
        sum1 = sum2 - 0.3 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
    elif 10 <= days <= 15:
        sum1 = sum2 - 0.35 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
    elif days > 15:
        sum1 = sum2 - 0.50 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
elif room == "president apartment":
    price += 35
    sum2 = price * (days - 1)
    if days < 10:
        sum1 = sum2 - 0.1 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
    elif 10 <= days <= 15:
        sum1 = sum2 - 0.15 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
    elif days > 15:
        sum1 = sum2 - 0.20 * sum2
        if feedback == "positive":
            final_sum = sum1 + (0.25 * sum1)
            print(f"{final_sum:.2f}")
        elif feedback == "negative":
            final_sum = sum1 - (0.1 * sum1)
            print(f"{final_sum:.2f}")
