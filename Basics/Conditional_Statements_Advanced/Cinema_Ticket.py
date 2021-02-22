# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	12	14	14	12	16	16

day = str(input())
if day == "Monday" or day == "Tuesday" or day == "Friday":
    print(12)
elif day == "Wednesday" or day == "Thursday":
    print(14)
else:
    print(16)

