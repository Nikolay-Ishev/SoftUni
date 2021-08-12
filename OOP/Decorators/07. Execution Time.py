from time import perf_counter


def exec_time(function):
    def wrapper(*args, **kwargs):
        tic = perf_counter()
        result = function(*args, **kwargs)
        toc = perf_counter()
        return toc - tic

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
