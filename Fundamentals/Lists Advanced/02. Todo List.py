importance_list = [0] * 10
notes = input()
priorities_list = []
notes_list = []
final_list = []
while notes != "End":
    tokens = notes.split('-')
    priority = int(tokens[0])
    note = tokens[1]
    priorities_list.append(priority)
    notes_list.append(note)
    notes = input()
while notes_list:
    min_index = priorities_list.index(min(priorities_list))
    final_list.append(notes_list.pop(min_index))
    priorities_list.pop(min_index)
print(final_list)



