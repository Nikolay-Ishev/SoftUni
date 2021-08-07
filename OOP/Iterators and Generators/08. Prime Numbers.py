def get_primes(int_list):
    prime_list = [x for x in int_list if prime_or_not(x)]
    for x in prime_list:
        yield x


def prime_or_not(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    return False


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
