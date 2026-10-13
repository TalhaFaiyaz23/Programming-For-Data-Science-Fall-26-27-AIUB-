# Problem Statememt : Create a list containing the marks of five courses. Display the total, average, highest mark, and lowest mark. Count the number of passed courses, using 50 as the pass mark.

# Solve :

# 1. Create a list containing the marks of five courses
marks = [78, 45, 92, 60, 88]

# 2. Calculate and display the total marks
total = sum(marks)
print(f"Total Marks: {total}")

# 3. Calculate and display the average mark
average = total / len(marks)
print(f"Average Mark: {average}")

# 4. Display the highest and lowest marks
print(f"Highest Mark: {max(marks)}")
print(f"Lowest Mark: {min(marks)}")

# 5. Count the number of passed courses
passed_count = 0
for mark in marks:
    if mark >= 50:
        passed_count += 1

print(f"Number of Passed Courses: {passed_count}")