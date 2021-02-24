substrings = input().split(", ")
word_list = input().split(", ")
final_list = []
for substring in range(len(substrings)):
    sub = substrings[substring]
    [final_list.append(sub) for s in word_list if sub in s]
no_dup = []
[no_dup.append(e) for e in final_list if e not in no_dup]
print(no_dup)
#no_dup = sorted(set(final_list), key=final_list.index)
#set ще извади дупликатите а sorted ще ги сортира по key, който в случая е индекса от предния лист)


