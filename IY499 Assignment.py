import tkinter as tk
from tkinter import messagebox
import json

class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Tracker")
        self.root.geometry("400x400")
        
        # Load existing data
        self.students = self.load_data()

        # UI Elements
        tk.Label(root, text="Student Name:").pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Grade (0-100):").pack(pady=5)
        self.grade_entry = tk.Entry(root)
        self.grade_entry.pack()

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_student).pack(pady=10)
        tk.Button(root, text="View All", command=self.show_students).pack(pady=5)
        tk.Button(root, text="Sort by Grade", command=self.sort_students).pack(pady=5)
        tk.Button(root, text="Save & Exit", command=self.save_and_exit).pack(pady=20)

    def add_student(self):
        name = self.name_entry.get()
        try:
            grade = float(self.grade_entry.get())
            if 0 <= grade <= 100:
                self.students.append({"name": name, "grade": grade})
                messagebox.showinfo("Success", f"Added {name}")
                self.name_entry.delete(0, tk.END)
                self.grade_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Grade must be 0-100")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for grade")

    def show_students(self):
        display_text = ""
        for s in self.students:
            display_text += f"{s['name']}: {s['grade']}\n"
        
        if not display_text:
            display_text = "No students found."
            
        messagebox.showinfo("Student List", display_text)

    def sort_students(self):
        # Bubble Sort logic remains the same!
        # # Sorting logic here
        n = len(self.students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.students[j]['grade'] < self.students[j + 1]['grade']:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]
        messagebox.showinfo("Sorted", "Students sorted by highest grade. Click 'View All' to see.")

    def load_data(self):
        try:
            with open("grades.json", "r") as f:
                return json.load(f)
        except:
            return []

    def save_and_exit(self):
        with open("grades.json", "w") as f:
            json.dump(self.students, f)
        self.root.destroy()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = GradeApp(root)
    root.mainloop()