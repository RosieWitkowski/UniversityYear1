import tkinter as tk 
from tkinter import messagebox 


def show_help():
    messagebox.showinfo('Help', 'Type a task in the bar, then use Add to add new task\nSelect a task from the display box then press Delete to remove the task\nMark Complete to mark as complete, or again to undo')

def add_task():
    task = task_entry.get().strip()
    if not task:
        # H2: Match between real world
        status.config(text='Type the name of the task in the top bar.', bg='Red')
        root.after(3000, lambda: status.config(**default_status))
        return
    task_box.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    task_entry.focus_set()
    status.config(text='Task added!', bg='Green')
    root.after(status_stall, lambda: status.config(**default_status))

def delete_task():
    selected = task_box.curselection()
    if not selected:
        status.config(text='Select a task before attempting this action.', bg='Red')
        root.after(status_stall, lambda: status.config(**default_status))
        return
    # H3: User Control and Freedom
    if messagebox.askyesno('Confirm', 'Delete this task?'):
        task_box.delete(selected[0])
        status.config(text='Task deleted!', bg='Green')
        root.after(status_stall, lambda: status.config(**default_status))
    else:
        status.config(text='Cancelled deletion!', bg='Green')
        root.after(status_stall, lambda: status.config(**default_status))

def mark_complete():
    selected = task_box.curselection()
    if not selected:
        status.config(text='Select a task before attempting this action.', bg='Red')
        root.after(status_stall, lambda: status.config(**default_status))
        return
    index = selected[0]
    name = task_box.get(index)
    if name.startswith('✓'):
        task_box.delete(index)
        task_box.insert(index, name[1:])
        status.config(text='Task already marked as complete, marking as incomplete.', bg='Orange')
        root.after(status_stall, lambda: status.config(**default_status))
    else:
        task_box.delete(index)
        task_box.insert(index, '✓' + name)
        status.config(text='Task marked as complete!', bg='Green')
        root.after(status_stall, lambda: status.config(**default_status))
    
root = tk.Tk()
root.title("To-Do")
root.geometry("420x480")
root.config(bg="Light Blue")

# Heading and Help, H10: Help and documentation, and H8: Minimilistic (pop-up)
basic_style = {'font': ('Calibri', 18), 'fg': 'White'}
tk.Label(root, text="My To-Do List", bg='Dark Blue', **basic_style).pack(fill=tk.X)
tk.Button(root, text='?', bg='Green', fg='White', command=show_help, width=5).place(relx=.9, rely=0)

tk.Label(root, text="Type task here:", font=('Calibri', 11), bg="Light Blue").pack(pady=5)
task_entry = tk.Entry(root, **basic_style, relief='sunken', bg='Dark Grey')
task_entry.pack(pady=10)

# H7: Flexibility/effeciency of use
task_entry.bind('<FocusIn>', lambda e: task_entry.delete(0, tk.END)) # Note lambda e added after feedback
root.bind('<Return>', lambda e: add_task())

# H4: Consistency
btn_style = {'font': ('Calbiri', 12), 'bg': 'Light Grey', 'relief': 'raised'}
btn_frame = tk.Frame(root, bg='Light Blue')
btn_frame.pack(pady=5)
tk.Button(btn_frame, **btn_style, text='Add Task', command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, **btn_style, text='Delete Task', command=delete_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, **btn_style, text='Mark Complete', command=mark_complete).grid(row=1, column=0, columnspan=2)


# H6: Recognition > recall 
box_frame = tk.Frame(root)
box_frame.pack(pady=5)
scrollbar = tk.Scrollbar(box_frame)
scrollbar.pack(side='right')
task_box = tk.Listbox(box_frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
task_box.pack()
scrollbar.config(command=task_box.yview)


# H1 Visibility and H9: Error Recovery
default_status = {'text': 'Status: Everything is OK!', 'bg': 'Light Grey'}
status_stall = 4000
status = tk.Label(root, **default_status)
status.pack(pady=5)


root.mainloop()