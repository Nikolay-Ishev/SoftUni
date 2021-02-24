tickets = input().split(", ")
tickets = [a.strip() for a in tickets]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    left = ticket[:10]
    right = ticket[10:]
    l_count = 0
    r_count = 0
    l_ele = None
    r_ele = None
    for e in left:
        if e == '@' or e == '#' or e == '$' or e == '^':
            if e != l_ele and l_count >= 6:
                continue
            elif e != l_ele:
                l_count = 1
                l_ele = e
            elif e == l_ele:
                l_count += 1
        elif l_count < 6:
            l_ele = None
            l_count = 0
    for e in right:
        if e == '@' or e == '#' or e == '$' or e == '^':
            if e != r_ele and r_count >= 6:
                continue
            if e != r_ele:
                r_count = 1
                r_ele = e
            else:
                r_count += 1
        elif r_count < 6:
            r_ele = None
            r_count = 0
    if l_count >= 6 and r_count >= 6 and l_ele == r_ele:
        if l_count == 10 and r_count == 10:
            print(f"ticket \"{ticket}\" - {10}{r_ele} Jackpot!")
        elif l_count <= r_count:
            print(f"ticket \"{ticket}\" - {l_count}{l_ele}")
        elif r_count <= l_count:
            print(f"ticket \"{ticket}\" - {r_count}{r_ele}")
    else:
        print(f"ticket \"{ticket}\" - no match")




