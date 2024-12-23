#Code to give Grade to the students
students = {
    "Sumit": "A",
    "Rohan": "B",
    "Aman": "A",
    "Priya": "A",
    "Neha": "B"
}

name = input("Enter the student's name: ")
grade = students.get(name, "Student not found")
print(f"Grade for {name}: {grade}")
