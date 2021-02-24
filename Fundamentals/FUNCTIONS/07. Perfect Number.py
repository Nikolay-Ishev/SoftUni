#A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself)
def perfect_number(a):
    divisors_sum = 0
    for divisor in range(1, a + 1):
        if a % divisor == 0:
            divisors_sum += divisor
    if a == divisors_sum / 2:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


input_a = int(input())
print(perfect_number(input_a))







