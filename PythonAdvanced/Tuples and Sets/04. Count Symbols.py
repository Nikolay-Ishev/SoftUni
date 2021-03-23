text = input()
ch_dict = {}
for el in text:
    if el not in ch_dict:
        ch_dict[el] = 0
    ch_dict[el] += 1
for key, value in sorted(ch_dict.items()):
    print(f"{key}: {value} time/s")

