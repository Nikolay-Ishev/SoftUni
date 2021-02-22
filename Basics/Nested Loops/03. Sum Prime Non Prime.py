command = input()
sum_prime = 0
sum_non_prime = 0
while command != "stop":
    number = int(command)
    count_divisions = 0
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for prime_non_prime in range(1, number + 1):
        if number % prime_non_prime == 0:
            count_divisions += 1
    if count_divisions <= 2:
        sum_prime += number
    elif count_divisions > 2:
        sum_non_prime += number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

