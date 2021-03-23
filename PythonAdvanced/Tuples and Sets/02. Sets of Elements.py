
set_1_length, set_2_length = input().split()
set_1 = set()
set_2 = set()
for _ in range(int(set_1_length)):
    set_1.add(input())
for _ in range(int(set_2_length)):
    set_2.add(input())
intersection = set_1 & set_2
for el in intersection:
    print(el)
