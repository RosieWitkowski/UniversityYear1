"""Exercise 4: To-Do List Application
Difficulty: Intermediate
Build a to-do list manager with the following features:
1. An Entry widget and "Add" button to add new tasks.
2. A Listbox displaying all current tasks with a Scrollbar.
3. A "Mark Done" button that adds "[DONE] " before the selected task text.
4. A "Delete" button that removes the selected task (with confirmation).
5. A "Clear Completed" button that removes all tasks marked as done.
Page 35
CIS1703 — Programming 2: GUI with tkinterPart 1: Tutorials
6. A status bar showing the total number of tasks and how many are completed.
7. Pressing the Enter key in the Entry widget should also add the task."""

import tkinter as tk 
from tkinter import messagebox

class Checklist():
    def __init__(self, root):
        self.root = root
        self.root.title("Checklist")
        self.root.geometry("800x500")
        self.root.config(bg="#6591ff")

        tk.Label(root, font=("Courier New", 20), text="Checklist", bg="Black", fg="White").pack(pady=5, fill=tk.X)
        
        # Help/Exit
        tk.Button(root, text="?", bg="Green", fg="White", font=("Arial", 10), command=self.show_help).place(relx=.9, rely=0, width=20)
        tk.Button(root, text="X", bg="Red", fg="White", font=("Arial", 10), command=self.exit_app).place(relx=.95, rely=0, width=20)

        # Add new
        container = tk.Frame(root)
        container.pack(pady=5)
        self.name_entry = tk.Entry(container, width=50)
        self.name_entry.grid(row=0, column=0, padx=10)
        name_button = tk.Button(container, text="Add", command=self.add_task)
        name_button.grid(row=0, column=1)

        self.name_entry.bind("<FocusIn>", lambda x: self.name_entry.delete(0, tk.END))
        self.name_entry.bind("<Return>", lambda x: self.add_task())

        # Display tasks
        list_frame = tk.Frame(root)
        list_frame.pack(pady=5)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right")
        self.listbox = tk.Listbox(list_frame, width=50, selectmode=tk.SINGLE,activestyle="none", yscrollcommand=scrollbar.set)
        self.listbox.pack()
        scrollbar.config(command=self.listbox.yview)

        # Delete/Clear
        controls = tk.Frame(root)
        controls.pack(pady=5)
        tk.Button(controls, text="Delete", bg="Red", command= self.delete_task).grid(row=0, column=0)
        tk.Button(controls, text="Mark Completed", bg="Green", command= self.complete_task).grid(row=0, column=1)
        tk.Button(controls, text="Clear Completed", command = self.clear_task).grid(row=0, column=2)

        # Status bar 
        self.status_bar = tk.Label(text="", bg="Grey")
        self.status_bar.pack(fill=tk.X, pady=5)
        self.completed, self.added = 0, 0
        self.completed_bar = tk.Label(text="0/0 Completed", bg="Green")
        self.completed_bar.pack(fill=tk.X)
    
    def update_progress(self):
        self.completed_bar.config(text=f"{self.completed}/{self.added} Completed")

    def show_help(self):
        messagebox.showinfo("Help", "Type the name for a task, then press Add to create a new task.\nSelect a task and then press Delete or Mark as complete.\nMarking an already complete task will undo this.")
        
    def exit_app(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.root.destroy()

    def add_task(self):
        task = self.name_entry.get().strip()
        if not task:
            self.status_bar.config(bg="Red", text="Please enter a name for your new task, before attempting to Add.'")
            return
        self.listbox.insert(tk.END,task)
        self.name_entry.delete(0, tk.END) # Clear entry box for convenience
        self.status_bar.config(bg="Green", text="New task added!")

        self.added += 1 
        self.update_progress()
        self.name_entry.focus_set()
    
    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            self.status_bar.config(bg="Red", text="Please select a task before attempting to delete.")
            return 
        if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
            self.added-=1 
            if self.listbox.get(selection[0]).startswith('[DONE]'):
                self.completed -= 1
            self.update_progress()
            self.listbox.delete(selection[0])
            self.status_bar.config(bg="Grey", text="Task deleted")
            

    def complete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            self.status_bar.config(bg="Red", text="Please select a task to mark as complete.")
            return False
        item = f"{self.listbox.get(selection)}"
        if item.startswith('[DONE]'):
            self.listbox.delete(selection)
            self.listbox.insert(selection, item[6:])
            self.completed -= 1
        else:
            self.listbox.delete(selection)
            self.listbox.insert(selection, '[DONE]' + item)
            self.completed += 1
        self.update_progress()

    def clear_task(self):
        if not self.listbox:
            self.status_bar.config(bg="Red", text="No tasks to sort.")
            return 
        
        self.status_bar.config(bg="Grey", text="Sorting... ")

        for index, item in reversed(list(enumerate(self.listbox.get(0, tk.END)))):
            if item.startswith('[DONE]'):
                self.listbox.delete(index)
                self.completed -= 1
                self.added -= 1 
                self.update_progress()

        self.status_bar.config(bg="Green", text="Sorted!")

if __name__ == "__main__":
    root = tk.Tk()
    checklist = Checklist(root)
    root.mainloop()