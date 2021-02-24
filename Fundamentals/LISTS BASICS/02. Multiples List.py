factor = int(input())
count = int(input())
list_n = 0
list_final = []
for n in range(count):
    list_n += factor
    list_final.append(list_n)
print(list_final)
