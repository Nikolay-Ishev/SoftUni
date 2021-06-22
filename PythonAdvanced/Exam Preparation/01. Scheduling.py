jobs = [int(x) for x in input().split(", ")]
jobs_list = [(v, i) for (i, v) in enumerate(jobs)]
last_task = int(input())
clock_cycles = 0
sorted_jobs = sorted(jobs_list)
# print(sorted_jobs)
for el in sorted_jobs:
    value, index = el
    clock_cycles += value
    if index == last_task:
        break
print(clock_cycles)

