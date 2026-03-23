# Aim: under 35 mins
import tkinter as tk 
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if not task or task == 'Type task name here, then press Add':
        status.config(text="Please enter a task.", bg="Red")
        return
    
    taskbox.insert(tk.END, task)
    
    # Reset entry box
    task_entry.delete(0, tk.END)
    task_entry.focus_set()

    status.config(text="Added task!", bg="Green")
    root.after(3000, lambda: status.config(text="", bg="Violet"))

def delete_task():
    selected = taskbox.curselection()
    # H5: Error prevention
    if not selected:
        status.config(text="No task selected!", bg="Red")
        return 
    
    # Confirmation for H5: Error Prevention
    if not messagebox.askyesno('Confirm', 'Are you sure you want to delete this task?'):
        status.config(text="Cancelled deletion.", bg="Green")
        root.after(300, status.config(text="", bg="Violet"))
        return 
    taskbox.delete(selected[0])
    status.config(text="Deleted!", bg="Green")
    root.after(300, status.config(text="", bg="Violet"))

def mark_complete():
    selected = taskbox.curselection()
    # H5: Error prevention
    if not selected:
        status.config(text="No task selected!", bg="Red")
        return 
    index = selected[0]
    name = taskbox.get(index)
    # H3: User control
    if name.startswith('✓'):
        taskbox.delete(index)
        taskbox.insert(index, name[1:])
        status.config(text="Task already completed, marked as incomplete", bg="Orange")
    else:
        taskbox.delete(index)
        taskbox.insert(index, '✓' + name)
        status.config(text="Task completed!", bg='Green')
    # root.after(3000, status.config(text="", bg="Violet"))
        
# Main Window
root = tk.Tk()
root.title('To-Do')
root.geometry("350x400")
root.config(bg="Violet")

tk.Label(root, text="My To-Do List", font=("Arial", 20), fg="White", bg="Pink").pack(fill=tk.X, pady=5)

# Entry bar for tasks, with bind for H7: Flexibility
task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=5)
task_entry.insert(0, 'Type task name here, then press Add')

task_entry.bind('<FocusIn>', lambda e: task_entry.delete(0, tk.END))
task_entry.bind('<Return>', lambda e: add_task())

# Buttons for H3: User Control
btn_style = {'font': ("Arial", 11), 'bg': 'Purple'}
btn_frame = tk.Frame(root, bg="Violet")
btn_frame.pack(pady=5)
tk.Button(btn_frame, **btn_style,text="Add Task", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, **btn_style, text="Delete Task", command=delete_task).grid(row=0, column=1)
tk.Button(btn_frame, **btn_style,text="Mark Complete", command=mark_complete).grid(row=1,column=0, columnspan=2)

# Listbox for H6: Recognition over recall
taskbox_frame = tk.Frame(root)
taskbox_frame.pack(pady=5)

scrollbar = tk.Scrollbar(taskbox_frame)
scrollbar.pack(side='right')
taskbox = tk.Listbox(taskbox_frame, width=32, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
taskbox.pack()
scrollbar.config(command=taskbox.yview)

tk.Label(root, text="Click a task to select, then use Delete or Mark Complete").pack(pady=5)

# Status label for H10: Help 
status = tk.Label(root, text="", bg="Violet")
status.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()