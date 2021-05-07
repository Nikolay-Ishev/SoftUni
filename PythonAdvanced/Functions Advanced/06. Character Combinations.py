def permute(text, current_index=0):
    if current_index == len(text):
        print(*text, sep="")
        return
    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        permute(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]
        # the above row is bringing the indexes how they were before the last swap


text=list(input())
permute(text)

#from itertools import permutations
#print(list(permutations(text)))
#returns iter object