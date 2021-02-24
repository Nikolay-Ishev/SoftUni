def odd_even_sum(a):
    odd_sum = 0
    even_sum = 0
    for element in str(a):
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


n = int(input())
print(odd_even_sum(n))
