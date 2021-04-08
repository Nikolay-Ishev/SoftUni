vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)
print("".join(x for x in input() if x not in vowels))
