import matplotlib.pyplot as plt

number_of_students = int(input("Enter total number of students: "))
number_of_subjects = int(input("Enter total number of subjects: "))

subjects = []

for x in range(number_of_subjects):
    subject = input(f"Enter subject {x + 1} name: ")
    subjects.append(subject)

students = []
students_total_marks = []
students_percentage = []
students_grade = []

for x in range(number_of_students):
    print(f"\nEnter details for student {x + 1}")

    name = input("Enter student name: ")
    students.append(name)

    total_marks = 0

    for subject in subjects:
        mark = float(input(f"Enter marks in {subject}: "))
        total_marks = total_marks + mark

    percentage = (total_marks / (number_of_subjects * 100)) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    students_total_marks.append(total_marks)
    students_percentage.append(percentage)
    students_grade.append(grade)

print("\n" + "=" * 78)
print("                         STUDENT MARK REPORT")
print("=" * 78)

print(
    f"{'STUDENT NAME':<20} | {'TOTAL MARK':<15} | "
    f"{'PERCENTAGE':<15} | {'GRADE':<10}"
)

print("-" * 78)

for x in range(number_of_students):
    print(
        f"{students[x]:<20} | "
        f"{students_total_marks[x]:<15.2f} | "
        f"{students_percentage[x]:<14.2f}% | "
        f"{students_grade[x]:<10}"
    )

print("=" * 78)

plt.figure(figsize=(8, 6))

plt.pie(
    students_total_marks,
    labels=students,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Students' Total Marks Distribution")
plt.axis("equal")
plt.show()
