from itertools import permutations


def possible_permutations(n_list):
    perm_list = all_perm(n_list)
    # perm_list = permutations(n_list)
    for el in perm_list:
        yield list(el)


def all_perm(seq):
    if len(seq) == 0:
        return []
    elif len(seq) == 1:
        return [seq]
    current_perm = []
    for i in range(len(seq)):
        el = seq[i]
        reminding_elements = seq[:i] + seq[i+1:]
        for sec_el in all_perm(reminding_elements):
            current_perm.append([el] + sec_el)
    return current_perm




[print(n) for n in possible_permutations([1, 2, 3])]
