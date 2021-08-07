def fibonacci():
    start = 1
    previous_n = 0
    while True:
        yield previous_n
        start += previous_n
        previous_n = start - previous_n


generator = fibonacci()
for i in range(6):
    print(next(generator))

