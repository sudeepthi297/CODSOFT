
import tkinter as tk
from tkinter import messagebox


# Create the main application window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("600x500")
root.configure(bg="#F2F6FC")
root.resizable(False, False)


# Store tasks in a Python list for Session 1
tasks = []


# Add a new task
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning(
            "Empty Task",
            "Please enter a task before adding."
        )
        return

    tasks.append(task)
    refresh_tasks()
    task_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Your task was added successfully!"
    )


# Display all tasks
def refresh_tasks():
    task_list.delete(0, tk.END)

    for number, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{number}. {task}")


# Create the title
title_label = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 24, "bold"),
    bg="#F2F6FC",
    fg="#243B53"
)
title_label.pack(pady=(20, 5))


# Create a subtitle
subtitle_label = tk.Label(
    root,
    text="Organize your day, one task at a time!",
    font=("Arial", 11),
    bg="#F2F6FC",
    fg="#526579"
)
subtitle_label.pack(pady=(0, 20))


# Create the task input field
task_entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=35,
    relief="solid",
    bd=1
)
task_entry.pack(pady=5, ipady=8)


# Create the Add Task button
add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    font=("Arial", 11, "bold"),
    bg="#2D8C76",
    fg="white",
    activebackground="#24745F",
    activeforeground="white",
    width=15,
    cursor="hand2"
)
add_button.pack(pady=10)


# Create the task list display area
task_list = tk.Listbox(
    root,
    font=("Arial", 12),
    width=48,
    height=12,
    bg="white",
    fg="#243B53",
    selectbackground="#B7E4D8",
    selectforeground="#243B53",
    relief="solid",
    bd=1
)
task_list.pack(pady=10)


# Start the application
root.mainloop()
