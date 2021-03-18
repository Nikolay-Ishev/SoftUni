queries = int(input())
stack = []
PUSH = "1"
DELETE = "2"
PRINT_MAX = "3"
PRINT_MIN = "4"
for n in range(queries):
    command = input()
    if command.startswith(PUSH):
        e = int(command.split()[1])
        stack.append(e)
    elif command.startswith(DELETE):
        if stack:
            stack.pop()
    elif command.startswith(PRINT_MAX):
        if stack:
            print(max(stack))
    elif command.startswith(PRINT_MIN):
        if stack:
            print(min(stack))
print(*reversed(stack), sep=", ")



