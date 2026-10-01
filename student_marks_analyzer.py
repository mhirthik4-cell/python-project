import matplotlib.pyplot as plt
import numpy as np

number_of_students = int(input("Enter total number of students: "))

students = []
students_marks = []

for x in range(number_of_students):
    name = input(f"Enter name of student {x + 1}: ")
    mark = float(input(f"Enter marks of {name}: "))

    students.append(name)
    students_marks.append(mark)

total = sum(students_marks)
average = total / number_of_students
maximum = max(students_marks)
minimum = min(students_marks)

topper_index = students_marks.index(maximum)
topper_name = students[topper_index]

print("\n----- STUDENT REPORT -----")
print("NUMBER OF STUDENTS:", number_of_students)
print("STUDENT NAMES:", students)
print("STUDENT MARKS:", students_marks)
print("TOTAL OF ALL MARKS:", total)
print("AVERAGE MARKS:", round(average, 2))
print("HIGHEST MARK:", maximum)
print("LOWEST MARK:", minimum)
print("TOPPER:", topper_name)

plt.figure(figsize=(8, 6))
plt.pie(
    students_marks,
    labels=students,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Students' Marks Distribution")
plt.axis("equal")
plt.show()
