# Problem Statement: Write a function named calculate_grade(marks) that receives a list of marks, calculates the average, and returns the corresponding grade.

# Solve : 

def calculate_grade(marks):

    # Calculate average
    average = sum(marks) / len(marks)
    
    # Determine grade based on the given criteria table
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

# Calling the function using a list of five marks
sample_marks = [82, 74, 91, 65, 88]
grade = calculate_grade(sample_marks)

print(f"Marks: {sample_marks}")
print(f"Calculated Grade: {grade}")