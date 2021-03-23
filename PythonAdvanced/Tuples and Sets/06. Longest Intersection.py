intersection = set()
for numbers in range(int(input())):
    a, b = input().split("-")
    start_a, end_a = a.split(",")
    start_b, end_b = b.split(",")
    set_a = set()
    set_b = set()
    for n in range(int(start_a), int(end_a) + 1):
        set_a.add(n)
    for n in range(int(start_b), int(end_b) + 1):
        set_b.add(n)
    ab_intersection = set_a & set_b
    if len(ab_intersection) > len(intersection):
        intersection = ab_intersection
print(f"Longest intersection is {list(intersection)} with length {len(intersection)}")


