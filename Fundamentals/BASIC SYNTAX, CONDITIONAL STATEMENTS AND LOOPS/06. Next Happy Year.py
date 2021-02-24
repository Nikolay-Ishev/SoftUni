year = int(input())
year += 1
happy_year = False
while not happy_year:
    if len(set(str(year))) == len(str(year)):
        happy_year = True
        print(year)
    else:
        year += 1



