import sys

n = int(input())
min_odd = sys.maxsize
max_odd = -sys.maxsize
min_even = sys.maxsize
max_even = -sys.maxsize
sum_even = 0
sum_odd = 0
for numbers in range(1, n + 1):
    num = float(input())
    if numbers % 2 == 0:
        sum_even += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    else:
        sum_odd += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num

print(f"OddSum={sum_odd:.2f},")
if min_odd == sys.maxsize:
    print("OddMin=No,")
elif min_odd != sys.maxsize:
    print(f"OddMin={min_odd:.2f},")
if max_odd == -sys.maxsize:
    print("OddMax=No,")
elif max_odd != -sys.maxsize:
    print(f"OddMax={max_odd:.2f},")
print(f"EvenSum={sum_even:.2f},")
if min_even == sys.maxsize:
    print("EvenMin=No,")
elif min_even != sys.maxsize:
    print(f"EvenMin={min_even:.2f},")
if max_even == -sys.maxsize:
    print("EvenMax=No")
elif max_even != -sys.maxsize:
    print(f"EvenMax={max_even:.2f}")



# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {"No"},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {"No"},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {"No"},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {"No"}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.



