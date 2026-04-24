import json
import os

# Student Class
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }


# Manager Class
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        # Check unique ID
        for s in self.students:
            if s["student_id"] == student.student_id:
                print("❌ Student ID already exists!")
                return
        self.students.append(student.to_dict())
        self.save_students()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No records found.")
            return
        for s in self.students:
            print(f"ID: {s['student_id']} | Name: {s['name']} | Grade: {s['grade']}")

    def update_student(self, student_id):
        for s in self.students:
            if s["student_id"] == student_id:
                s["name"] = input("Enter new name: ")
                s["grade"] = input("Enter new grade: ")
                self.save_students()
                print("✅ Student updated!")
                return
        print("❌ Student not found!")

    def delete_student(self, student_id):
        for s in self.students:
            if s["student_id"] == student_id:
                self.students.remove(s)
                self.save_students()
                print("✅ Student deleted!")
                return
        print("❌ Student not found!")


# CLI Menu
def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            student_id = input("Enter ID: ")
            grade = input("Enter grade: ")
            student = Student(name, student_id, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = input("Enter ID to update: ")
            manager.update_student(student_id)

        elif choice == "4":
            student_id = input("Enter ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()