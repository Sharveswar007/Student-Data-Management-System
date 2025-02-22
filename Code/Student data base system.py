import pandas as pd


class Student:
    def __init__(self, name, roll_number, age, course, grade, email):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.course = course
        self.grade = grade
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nRoll No: {self.roll_number}\nAge: {self.age}\nCourse: {self.course}\nGrade: {self.grade}\nEmail: {self.email}"


import csv


def add_student(student):
    with open("students.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student.name,
            student.roll_number,
            student.age,
            student.course,
            student.grade,
            student.email
        ])


def delete_student(roll_number):
    students = []
    with open("students.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != roll_number:  
                students.append(row)

    with open("students.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)


def get_student(roll_number):
    with open("students.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == roll_number:  
                return Student(*row)
        return None


def update_student(student):
    students = []
    with open("students.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == student.roll_number:  
                students.append([
                    student.name,
                    student.roll_number,
                    student.age,
                    student.course,
                    student.grade,
                    student.email
                ])
            else:
                students.append(row)

    with open("students.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)


def load_students():
    students = []
    with open("students.csv", mode="r") as file:
        reader = csv.reader(file)
        header = next(reader, None)  
        if header is None:
           return students

        for row in reader:
            if len(row) == 6:
                student = Student(*row)
                students.append(student)
            else:
                print(f"Skipping invalid student record: {row}")

    return students


def main():
    print("Welcome to the Student Data Management System!")

    while True:
        print("\n1. Add Student\n2. Update Student\n3. Delete Student\n4. Search Student\n5. Generate Report\n6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            age = input("Enter age: ")
            course = input("Enter course: ")
            grade = input("Enter grade: ")
            email = input("Enter email: ")

            student = Student(name, roll_number, age, course, grade, email)
            add_student(student)
            print("Student added successfully!")

        elif choice == "2":
            roll_number = input("Enter roll number of the student to update: ")
            student = get_student(roll_number)
            if student:
                print(f"Updating details for {student}")
                name = input("Enter updated name: ")
                age = input("Enter updated age: ")
                course = input("Enter updated course: ")
                grade = input("Enter updated grade: ")
                email = input("Enter updated email: ")

                student.name = name
                student.age = age
                student.course = course
                student.grade = grade
                student.email = email
                update_student(student)
                print("Student details updated successfully!")
            else:
                print("Student not found!")

        elif choice == "3":
            roll_number = input("Enter roll number of the student to delete: ")
            student = get_student(roll_number)
            if student:
                delete_student(roll_number)
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        elif choice == "4":
            roll_number = input("Enter roll number of the student to search: ")
            student = get_student(roll_number)
            if student:
                print(f"Student found: {student}")
            else:
                print("Student not found!")

        elif choice == "5":
            students = load_students()
            print("Generating student report:")
            data = pd.read_csv("students.csv")
            print(data)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
