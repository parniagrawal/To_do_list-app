import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)

add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()
