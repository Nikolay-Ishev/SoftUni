n = int(input())
syn_dic = {}
for i in range(n):
    key = input()
    value = input()
    if key not in syn_dic:
        syn_dic[key] = []
    syn_dic[key].append(value)
for key, value in syn_dic.items():
    print(f"{key} - {', '.join(value)}")



