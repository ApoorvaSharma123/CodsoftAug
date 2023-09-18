import tkinter as tk

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create and configure the add and remove buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Create and configure the listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack()

# Start the GUI main loop
root.mainloop()
