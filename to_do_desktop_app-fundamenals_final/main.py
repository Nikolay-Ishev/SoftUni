from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from tkinter.scrolledtext import *
from tkinter.messagebox import *
import json

all_tasks_to_write = []


def get_all_tasks_from_file():
    with open("db.txt", "r") as file:
        try:
            existing_tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_tasks = []
    return existing_tasks


def write_tasks_to_file(all_tasks):
    with open("db.txt", "r+") as file:
        existing_tasks = get_all_tasks_from_file()
        file.seek(0)
        file.truncate()
        all_tasks.extend(existing_tasks)
        json.dump(all_tasks, file)
        all_tasks_to_write.clear()


def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()


def trigger_edit_task(selected, **kwargs):
    m = askquestion("Edit", "Are you sure you want to edit?")
    if m == "yes":
        existing_tasks = get_all_tasks_from_file()
        existing_tasks.remove(selected)
        with open("db.txt", "r+") as file:
            file.seek(0)
            file.truncate()
            json.dump(existing_tasks, file)
            all_tasks_to_write.clear()
        all_tasks_to_write.append(kwargs)
        save_and_exit(tk)


def edit_task(tk, selected):
    selected = eval(selected)
    clear_view(tk)
    Label(tk, text="Enter your task name: ").grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry(tk)
    task_name.grid(row=0, column=1, padx=20, pady=20)
    task_name.delete(0, END)
    task_name.insert(0, selected['name'])
    Label(tk, text="Due date: ").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.grid(row=1, column=1)
    date.delete(0, END)
    date.insert(0, selected['date'])
    Label(tk, text="Description: ").grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(tk, width=50, height=10)
    description.grid(row=2, column=1, padx=20, pady=20)
    description.insert(INSERT, selected['description'])
    description.insert(END, "")
    Label(tk, text="Select priority: ").grid(row=3, column=0, padx=20, pady=20)
    selected_priority_num = IntVar()
    selected_priority_num.set(int(selected['priority']))
    button_frame = Frame(tk)
    button_frame.grid(row=3, column=1)
    Radiobutton(button_frame, text="Low", value=1, variable=selected_priority_num).grid(row=0, column=1, padx=20,
                                                                                        pady=20)
    Radiobutton(button_frame, text="Medium", value=2, variable=selected_priority_num).grid(row=0, column=2, padx=20,
                                                                                           pady=20)
    Radiobutton(button_frame, text="High", value=3, variable=selected_priority_num).grid(row=0, column=3, padx=20,
                                                                                         pady=20)
    Label(tk, text="Completed: ").grid(row=4, column=0, padx=20, pady=20)
    is_completed = BooleanVar()
    is_completed.set(selected['is_completed'])
    Checkbutton(tk, text="Check", variable=is_completed).grid(row=4, column=1, padx=20, pady=20)
    Button(tk, text="Edit task", bg="grey", fg="white",
           command=lambda: trigger_edit_task(selected, name=task_name.get(), date=date.get(),
                                             description=description.get("1.0", END),
                                             priority=selected_priority_num.get(),
                                             is_completed=is_completed.get())).grid(
        row=5, column=0, padx=20, pady=80)
    Button(tk, text="Back to main menu", bg="grey", fg="white",
           command=lambda: save_and_exit(tk)).grid(row=5, column=1, padx=20, pady=80)


def delete_task(tk, value):
    m = askquestion("Delete", "Are you sure you want to delete?")
    if m == "yes":
        existing_tasks = get_all_tasks_from_file()
        existing_tasks.remove(eval(value))
        with open("db.txt", "r+") as file:
            file.seek(0)
            file.truncate()
            json.dump(existing_tasks, file)
            all_tasks_to_write.clear()
    render_list_task_view(tk)


def render_list_task_view(tk):
    clear_view(tk)
    box = Combobox(tk, width=110)
    existing_tasks = get_all_tasks_from_file()
    box['values'] = existing_tasks
    box.grid(row=0, column=0, padx=10, pady=10)
    button_frame = Frame(tk)
    button_frame.grid(row=1, column=0, pady=20)
    Button(button_frame, text="View / Edit", bg="grey", fg="White",
           command=lambda: edit_task(tk, box.get())).grid(
        row=2,
        column=0,
        pady=20,
        padx=30)
    Button(button_frame, text="Delete", bg="grey", fg="White",
           command=lambda: delete_task(tk,
                                       box.get())).grid(row=2, column=1, pady=20, padx=30)

    Button(button_frame, text="Back to main menu", fg="White", bg="grey",
           command=lambda: save_and_exit(tk)).grid(row=2, column=2, pady=20, padx=30)


def create_task(**kwargs):
    all_tasks_to_write.append(kwargs)
    save_and_exit(tk)


def save_and_exit(tk):
    write_tasks_to_file(all_tasks_to_write)
    clear_view(tk)
    render_main_view(tk)


def render_create_task_view(tk):
    clear_view(tk)
    Label(tk, text="Enter your task name: ").grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry(tk)
    task_name.grid(row=0, column=1, padx=20, pady=20)
    Label(tk, text="Due date: ").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.grid(row=1, column=1)
    Label(tk, text="Description: ").grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(tk, width=50, height=10)
    description.grid(row=2, column=1, padx=20, pady=20)
    Label(tk, text="Select priority: ").grid(row=3, column=0, padx=20, pady=20)
    selected_priority_num = IntVar()
    button_frame = Frame(tk)
    button_frame.grid(row=3, column=1)
    Radiobutton(button_frame, text="Low", value=1, variable=selected_priority_num).grid(row=0, column=1, padx=20,
                                                                                        pady=20)
    Radiobutton(button_frame, text="Medium", value=2, variable=selected_priority_num).grid(row=0, column=2, padx=20,
                                                                                           pady=20)
    Radiobutton(button_frame, text="High", value=3, variable=selected_priority_num).grid(row=0, column=3, padx=20,
                                                                                         pady=20)
    Label(tk, text="Completed: ").grid(row=4, column=0, padx=20, pady=20)
    is_completed = BooleanVar()
    Checkbutton(tk, text="Check", variable=is_completed).grid(row=4, column=1, padx=10, pady=20)
    another_button_frame = Frame(tk)
    another_button_frame.grid(row=5, column=1)
    Button(another_button_frame, text="Create task", bg="grey", fg="white", height=5, width=20,
           command=lambda: create_task(name=task_name.get(), date=date.get(), description=description.get("1.0", END),
                                       priority=selected_priority_num.get(), is_completed=is_completed.get())).grid(
        row=0, column=0, padx=20, pady=10)
    Button(another_button_frame, text="Back to main menu", bg="grey", fg="white", height=5, width=20,
           command=lambda: save_and_exit(tk)).grid(row=0, column=1, padx=10, pady=10)


def render_main_view(tk):
    a = Button(tk, text="List tasks", bg="grey", fg="white", height=5, width=30, font='Helvetica',
               command=lambda: render_list_task_view(tk)).grid(row=0, column=0, padx=30, pady=50)

    b = Button(tk, text="Create task", bg="grey", fg="white", height=5, width=30, font='Helvetica',
               command=lambda: render_create_task_view(tk)).grid(row=0, column=3, padx=30, pady=50)


tk = Tk()
tk.geometry("700x600")
# tk.configure(bg='black')
render_main_view(tk)

tk.mainloop()
