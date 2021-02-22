n = int(input())
even = 0
odd = 0
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num
# "Yes" и на нов ред "Sum = " + сумата; иначе да се отпечата "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.
if even == odd:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {abs(even - odd)}")



