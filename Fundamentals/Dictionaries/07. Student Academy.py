n = int(input())
students = {}
for pair in range(n):
    key = input()
    value = float(input())
    if key not in students:
        students[key] = []
    students[key].append(value)
best_students = dict(filter(lambda x: sum(x[1]) / len(x[1]) >= 4.5, students.items()))
av_best_st = {}
for key, value in best_students.items():
    av_best_st[key] = sum(value) / len(value)
best_st_sorted = dict(sorted(av_best_st.items(), key=lambda x: -x[1]))
for key, value in best_st_sorted.items():
    print(f"{key} -> {value:.2f}")
