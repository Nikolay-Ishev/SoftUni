def el_formula(n):
    return 2 * (n ** 2)


shell_counter = 0
shell_list = []
electrons = int(input())
while electrons > 0:
    shell_counter += 1
    shell_fill = el_formula(shell_counter)
    if shell_fill <= electrons:
        electrons -= shell_fill
        shell_list.append(shell_fill)
    else:
        shell_list.append(electrons)
        electrons = 0
print(shell_list)





