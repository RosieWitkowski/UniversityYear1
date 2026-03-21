"""import tkinter as tk
from tkinter import messagebox
class StudentManager:
    def __init__(self, root):
    self.root = root
    self.root.title("Student Record Manager -- CIS1703")
    self.root.geometry("600x500")
    self.root.configure(bg="#f5f5f5")
    self.students = []
    self.create_menu()
    self.create_header()
    self.create_form()
    self.create_list_section()
    self.create_status_bar()
def create_menu(self):
menu_bar = tk.Menu(self.root)
self.root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear All", command=self.clear_all)
file_menu.add_separator()
Page 28
CIS1703 — Programming 2: GUI with tkinterPart 1: Tutorials
file_menu.add_command(label="Exit", command=self.root.quit)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=self.show_about)
def create_header(self):
header = tk.Frame(self.root, bg="#5B2C8E", height=50)
header.pack(fill=tk.X)
header.pack_propagate(False)
tk.Label(header, text="Student Record Manager",
font=("Arial", 16, "bold"), bg="#5B2C8E",
fg="white").pack(expand=True)
def create_form(self):
form = tk.LabelFrame(self.root, text="Add New Student",
font=("Arial", 11, "bold"), bg="#f5f5f5", padx=10, pady=10)
form.pack(fill=tk.X, padx=15, pady=10)
# Row 0: Name
tk.Label(form, text="Name:", font=("Arial", 10),
bg="#f5f5f5").grid(row=0, column=0, pady=3, sticky="e")
self.name_entry = tk.Entry(form, font=("Arial", 10), width=20)
self.name_entry.grid(row=0, column=1, pady=3, padx=5)
# Row 0: Student ID
tk.Label(form, text="Student ID:", font=("Arial", 10),
bg="#f5f5f5").grid(row=0, column=2, pady=3, sticky="e")
self.id_entry = tk.Entry(form, font=("Arial", 10), width=15)
self.id_entry.grid(row=0, column=3, pady=3, padx=5)
# Row 1: Course
tk.Label(form, text="Course:", font=("Arial", 10),
bg="#f5f5f5").grid(row=1, column=0, pady=3, sticky="e")
self.course_entry = tk.Entry(form, font=("Arial", 10), width=20)
self.course_entry.grid(row=1, column=1, pady=3, padx=5)
# Row 1: Grade
tk.Label(form, text="Grade:", font=("Arial", 10),
bg="#f5f5f5").grid(row=1, column=2, pady=3, sticky="e")
self.grade_var = tk.StringVar(value="B")
grades = ["A", "B", "C", "D", "F"]
grade_frame = tk.Frame(form, bg="#f5f5f5")
Page 29
CIS1703 — Programming 2: GUI with tkinterPart 1: Tutorials
grade_frame.grid(row=1, column=3, pady=3, padx=5)
for g in grades:
tk.Radiobutton(grade_frame, text=g, variable=self.grade_var,
value=g, bg="#f5f5f5", font=("Arial", 9)
).pack(side=tk.LEFT)
# Buttons
btn_frame = tk.Frame(form, bg="#f5f5f5")
btn_frame.grid(row=2, column=0, columnspan=4, pady=8)
tk.Button(btn_frame, text="Add Student", command=self.add_student,
bg="#5B2C8E", fg="white", font=("Arial", 10, "bold"),
width=12).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Remove Selected",
command=self.remove_student, width=14,
font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
def create_list_section(self):
list_frame = tk.LabelFrame(self.root, text="Student Records",
font=("Arial", 11, "bold"), bg="#f5f5f5", padx=10, pady=10)
list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
self.listbox = tk.Listbox(
list_frame,
font=("Courier", 10),
selectmode=tk.SINGLE,
yscrollcommand=scrollbar.set
)
self.listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=self.listbox.yview)
def create_status_bar(self):
self.status_var = tk.StringVar(value="Ready -- 0 students")
tk.Label(self.root, textvariable=self.status_var,
relief="sunken", anchor="w", font=("Arial", 9),
bg="#e0e0e0").pack(fill=tk.X)
def add_student(self):
name = self.name_entry.get().strip()
sid = self.id_entry.get().strip()
course = self.course_entry.get().strip()
Page 30
CIS1703 — Programming 2: GUI with tkinterPart 1: Tutorials
grade = self.grade_var.get()
if not name or not sid or not course:
messagebox.showwarning("Missing Data",
"Please fill in all fields.")
return
record = f"{sid:<12} {name:<20} {course:<15} {grade}"
self.students.append(record)
self.listbox.insert(tk.END, record)
# Clear form
self.name_entry.delete(0, tk.END)
self.id_entry.delete(0, tk.END)
self.course_entry.delete(0, tk.END)
self.name_entry.focus()
count = len(self.students)
self.status_var.set(f"Student added -- {count} student(s) total")
def remove_student(self):
selection = self.listbox.curselection()
if not selection:
messagebox.showinfo("Info", "Please select a student to
remove.")
return
if messagebox.askyesno("Confirm", "Remove selected student?"):
idx = selection[0]
self.listbox.delete(idx)
self.students.pop(idx)
count = len(self.students)
self.status_var.set(f"Student removed -- {count} student(s)
total")
def clear_all(self):
if messagebox.askyesno("Clear All", "Remove all student records?"):
self.listbox.delete(0, tk.END)
self.students.clear()
self.status_var.set("All records cleared -- 0 students")
def show_about(self):
messagebox.showinfo("About",
"Student Record Manager\nCIS1703 -- Programming 2\nVersion
Page 31
CIS1703 — Programming 2: GUI with tkinterPart 1: Tutorials
1.0")
# --- Main ---
if __name__ == "__main__":
root = tk.Tk()
app = StudentManager(root)
root.mainloop()"""