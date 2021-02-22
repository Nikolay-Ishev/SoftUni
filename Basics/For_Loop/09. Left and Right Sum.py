n = int(input())
left_sum = 0
right_sum = 0
for i in range(n):
    number = int(input())
    left_sum += number
for j in range(n):
    num = int(input())
    right_sum += num
# " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
