# Prpblem Statement : Using the student records above, display each student’s name and marks. Count the students who passed (marks ≥ 50), calculate the class average, and identify the student with the highest mark.


#Solve :

students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

passed_count = 0
total_marks = 0
highest_mark = -1
top_student = ""

# Display each student's name and marks, and gather analysis data
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")
    
    # Count passed students (marks >= 50)
    if student["marks"] >= 50:
        passed_count += 1
        
    # Accumulate total marks for average calculation
    total_marks += student["marks"]
    
    # Identify the student with the highest mark
    if student["marks"] > highest_mark:
        highest_mark = student["marks"]
        top_student = student["name"]

class_average = total_marks / len(students)

print("\n--- Analysis Summary ---")
print(f"Total Students Passed: {passed_count}")
print(f"Class Average Marks: {class_average:.2f}")
print(f"Highest Mark Holder: {top_student} with {highest_mark} marks")