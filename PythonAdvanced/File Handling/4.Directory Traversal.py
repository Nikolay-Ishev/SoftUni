import os

dir_dict = {}

# create a list with the files only
files = [el for el in os.listdir() if os.path.isfile(el)]

# create a dictionary with key - extension and value - list of the files with the specific extension
for file in files:
    for i in range(len(file) - 1, -1, -1):
        if file[i] == ".":
            extension = file[i:]
            break
    if extension not in dir_dict:
        dir_dict[extension] = []
    dir_dict[extension].append(file)

sorted_dir_dict = dict(sorted(dir_dict.items(), key=lambda x: x[0]))

# finds the desktop path for windows and linux
desktop_path = desktop = os.path.expanduser("~/Desktop")

# create a file on the desctop and extract the information from the sorted dictionary
with open(f"{desktop_path}\\report.txt", "w") as file:
    for key, value in sorted_dir_dict.items():
        file.write(f"{key}\n")
        for el in value:
            file.write(f"- - - {el}\n")
