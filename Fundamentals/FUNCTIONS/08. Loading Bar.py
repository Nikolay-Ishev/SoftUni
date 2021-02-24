def loading_bar(n):
    bar = "0% [..........]".split()
    complete = False
    if n == 100:
        complete = True
    else:
        bar[0] = f"{n}%"
        percent_index = n / 10
        bar[1] = f"[{int(percent_index) * '%'}{int(10 - percent_index) * '.'}]"
    if complete:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f"{bar[0]} {bar[1]}")
        print("Still loading...")


input_n = int(input())
loading_bar(input_n)
