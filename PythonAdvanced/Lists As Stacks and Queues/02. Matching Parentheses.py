expression = input()
open_brackets = []
for i in range(len(expression)):
    if expression[i] == "(":
        open_brackets.append(i)
    elif expression[i] == ")":
        beginning = int(open_brackets.pop())
        print(expression[beginning:i+1])
