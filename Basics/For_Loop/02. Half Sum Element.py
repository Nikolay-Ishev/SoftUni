import sys
numbers = int(input())
max_sum = -sys.maxsize
sum_1 = 0
for n in range(numbers):
    num = int(input())
    sum_1 += num
    if num > max_sum:
        max_sum = num
if max_sum == sum_1 - max_sum:
    print("Yes")
    print(f"Sum = {max_sum}")
else:
    print("No")
    print(f"Diff = {(abs(max_sum - (sum_1 - max_sum)))}")
