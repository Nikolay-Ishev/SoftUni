def list_duplicates(seq):
  seen = []
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set(x for x in seq if x in seen or seen.append(x))
  # turn the set into a list (as requested)
  return list( seen_twice )

def list_dups(seq):
    return list(set(x for x in seq if seq.count(x) > 1))


a = [1,2,3,2,1,5,6,5,5,5]
print(list_duplicates(a)) # yields [1, 2, 5]
print(list_dups(a))

