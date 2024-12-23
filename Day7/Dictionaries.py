#Code to study dictionarys and their various operations
#Creating a dictionary of students with their grades and cities
students = {
    "Sumit": {"grade": "A", "city": "Delhi"},
    "Rohan": {"grade": "B", "city": "Mumbai"},
    "Aman": {"grade": "A", "city": "Bangalore"}
}

#1.Accessing and printing details of a specific student
print("Details of Sumit:", students.get("Sumit", "Not Found"))

#2.Adding a new student
students["Priya"] = {"grade": "A", "city": "Chennai"}
print("\nAdded a new student: Priya")

#3.Updating a student's grade
students["Rohan"]["grade"] = "A"
print("\nUpdated Rohan's grade to 'A'.")

#4.Removing a student
removed_student = students.pop("Aman", "Not Found")
print("\nRemoved student Aman:", removed_student)

#5.Checking if a student exists
student_to_check = "Rohan"
if student_to_check in students:
    print(f"\n{student_to_check} exists in the dictionary.")
else:
    print(f"\n{student_to_check} does not exist in the dictionary.")

#6.Iterating through students
print("\nIterating through all students:")
for name, details in students.items():
    print(f"{name}: Grade {details['grade']}, City {details['city']}")

#7.Merging with another dictionary
new_students = {
    "Neha": {"grade": "B", "city": "Kolkata"},
    "Vikas": {"grade": "C", "city": "Pune"}
}
students.update(new_students)
print("\nMerged new students into the dictionary.")

#8.Using dictionary comprehension to list grades
grades = {name: details["grade"] for name, details in students.items()}
print("\nGrades of all students:", grades)

#9.Working with nested dictionaries
print("\nDetails of all students with nested dictionary:")
for name, info in students.items():
    print(f"Name: {name}, Grade: {info['grade']}, City: {info['city']}")

#10.Clearing the dictionary
print("\nClearing all student records.")
students.clear()
print("All students cleared:", students)
