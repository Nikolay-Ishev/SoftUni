n = int(input())
elements = set()
for _ in range(n):
    el_str = input().split()
    for e in el_str:
        elements.add(e)

for el in elements:
    print(el)

