odd_set = set()
even_set = set()
for x in range(int(input())):
    name = input()
    name_sum = 0
    for n in name:
        name_sum += ord(n)
    number = int(name_sum / (x + 1))
    if number % 2 == 0:
        even_set.add(number)
    else:
        odd_set.add(number)
even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    print(*(odd_set | even_set), sep=", ")
elif odd_sum > even_sum:
    print(*(odd_set - even_set), sep=", ")
else:
    print(*(odd_set ^ even_set), sep=", ")
