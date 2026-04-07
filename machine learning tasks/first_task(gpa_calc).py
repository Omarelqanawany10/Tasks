import tkinter as tk
from tkinter import messagebox

def grade_to_points(grade):
    if grade >= 90:
        return 4.0, "A"
    elif grade >= 85:
        return 3.7, "A-"
    elif grade >= 80:
        return 3.3, "B+"
    elif grade >= 75:
        return 3.0, "B"
    elif grade >= 70:
        return 2.7, "B-"
    elif grade >= 65:
        return 2.3, "C+"
    elif grade >= 60:
        return 2.0, "C"
    elif grade >= 55:
        return 1.7, "C-"
    elif grade >= 50:
        return 1.0, "D"
    else:
        return 0.0, "F"


def final_gpa_letter(gpa):
    if gpa >= 3.7:
        return "A"
    elif gpa >= 3.3:
        return "A-"
    elif gpa >= 3.0:
        return "B+"
    elif gpa >= 2.7:
        return "B"
    elif gpa >= 2.3:
        return "B-"
    elif gpa >= 2.0:
        return "C+"
    elif gpa >= 1.7:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"


def calculate_gpa():
    try:
        n = int(courses_entry.get())
        total_points = 0
        total_credits = 0
        result_text.delete("1.0", tk.END)

        for i in range(n):
            name = entries[i][0].get()
            grade = float(entries[i][1].get())
            credit = int(entries[i][2].get())

            points, letter = grade_to_points(grade)
            course_points = points * credit

            total_points += course_points
            total_credits += credit

            result_text.insert(
                tk.END,
                f"{name}: Course Points = {course_points}, Grade = {letter}\n"
            )

        gpa = total_points / total_credits
        final_letter = final_gpa_letter(gpa)

        result_text.insert(
            tk.END,
            f"\nTotal GPA = {round(gpa, 2)}\nFinal Grade = {final_letter}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid data")


def create_course_inputs():
    for widget in courses_frame.winfo_children():
        widget.destroy()

    entries.clear()
    n = int(courses_entry.get())

    tk.Label(courses_frame, text="Course Name").grid(row=0, column=1)
    tk.Label(courses_frame, text="Grade").grid(row=0, column=2)
    tk.Label(courses_frame, text="Credit Hours").grid(row=0, column=3)

    for i in range(n):
        tk.Label(courses_frame, text=f"Course {i+1}").grid(row=i+1, column=0)

        name = tk.Entry(courses_frame)
        grade = tk.Entry(courses_frame)
        credit = tk.Entry(courses_frame)

        name.grid(row=i+1, column=1)
        grade.grid(row=i+1, column=2)
        credit.grid(row=i+1, column=3)

        entries.append((name, grade, credit))

root = tk.Tk()
root.title("GPA Calculator - C System")

tk.Label(root, text="Number of Courses").pack()
courses_entry = tk.Entry(root)
courses_entry.pack()

tk.Button(root, text="Add Courses", command=create_course_inputs).pack()

courses_frame = tk.Frame(root)
courses_frame.pack()

tk.Button(root, text="Calculate GPA", command=calculate_gpa).pack()

result_text = tk.Text(root, height=12, width=60)
result_text.pack()

entries = []

root.mainloop()
