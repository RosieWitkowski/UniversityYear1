import tkinter as tk

root = tk.Tk()
root.title("Student Grades Tracker")
root.geometry("750x750")
root.config(bg="#70eaf3")

students = []
students_str = ""

def add_student():
    # name, grade = name.get(), grade.get()
    name = student_name.get()
    student_grade = grade.get()
    
    if not name:
        return name_label.config(text="Error: Input cannot be empty")
    
    try:
        student_grade = float(student_grade)
    except ValueError:
        return grade_label.config(text="Error: Please enter a number for grade")
    if student_grade > 100 or student_grade < 0:
        return grade_label.config(text="Error: Grade must be between 0 and 100")
        
    students.append((name, student_grade))
    display.config(text=students)

    # Re-config labels in case of previous incorrect input
    name_label.config(text="Student Name")
    grade_label.config(text="Grade(0-100)")

def average_grade():
    if not students:
        return display2.config(text="Error: No students found", fg="Red")
    marks =[mark for name, mark in students]
    avg = sum(marks) / len(marks)
    if avg >= 70:
        display2.config(text=f"Average grade: {avg:.2f} (Distinction!) Excellent!", fg="Green")
    elif avg >= 50:
        display2.config(text=f"Average grade: {avg:.2f} (Pass) Well done!", fg="Green")
    else:
        display2.config(text=f"Average grade: {avg:.2f} (Fail!) Requires improvement.", fg="Red")
        

# Adding students
name_label = tk.Label(root, text="Student Name")
name_label.pack(pady=10)
student_name = tk.Entry(root, font=("Arial", 12))
student_name.pack(pady=5)

grade_label = tk.Label(root, text="Grade(0-100)")
grade_label.pack(pady=10)
grade = tk.Entry(root)
grade.pack(pady=5)

tk.Button(root, text="Add Student", command=add_student).pack(pady=10)

display = tk.Label(root, bg="#70eaf3")
display.pack(pady=10)

# Displaying average
tk.Button(root, text="Average Grade", command=average_grade).pack(pady=10)
display2 = tk.Label(root, bg="#70eaf3")
display2.pack(pady=10)


tk.mainloop()