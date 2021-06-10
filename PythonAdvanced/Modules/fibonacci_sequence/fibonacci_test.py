from f_sequence import fibonacci_sequence

arguments = input().split()
while arguments[0] != "Stop":
    fibonacci_sequence(arguments)
    arguments = input().split()
