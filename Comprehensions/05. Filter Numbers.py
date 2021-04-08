start_n = int(input())
end_n = int(input())
print([x for x in range(start_n, end_n + 1) if any(x % divisor == 0 for divisor in range(2, 10))])
#
# for divisor in range(2, 10):
#     for x in range(start_n, end_n + 1):
#         print(x % divisor == 0)
