n = int(input())
positives = []
negatives = []
count_positives = 0
sum_negatives = 0
for integer in range(n):
    current_integer = int(input())
    if current_integer >= 0:
        count_positives += 1
        positives.append(current_integer)
    else:
        sum_negatives += current_integer
        negatives.append(current_integer)
print(positives)
print(negatives)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_negatives}")
