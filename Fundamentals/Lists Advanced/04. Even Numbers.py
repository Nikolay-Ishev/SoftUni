numbers = input().split(', ')
result = []
result_2 = []
#numbers = [int(num) for num in numbers]
numbers = list(map(lambda x: int(x), numbers))
[result.append(i) for i in range(len(numbers)) if numbers[i] % 2 == 0]
[result_2.append(i) for i, j in enumerate(numbers) if j % 2 == 0]
print(result)
print(result_2)
