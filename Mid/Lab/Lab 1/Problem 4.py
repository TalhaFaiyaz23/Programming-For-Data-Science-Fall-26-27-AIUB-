#defining a class to represent a student's marks

class StudentMarks:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        average = self.get_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        elif average < 50:
            return 'F'

    def total_marks(self):
        return sum(self.marks)

    def highest_mark(self):
        return max(self.marks)

    def lowest_mark(self):
        return min(self.marks)

    def passed(self):
        return all(mark >= 50 for mark in self.marks)

    def all_results(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average()}")
        print(f"Grade: {self.get_grade()}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Highest Mark: {self.highest_mark()}")
        print(f"Lowest Mark: {self.lowest_mark()}")
        print(f"Passed: {'Yes' if self.passed() else 'No'}")


if __name__ == "__main__":
        
        # creating a list of students with their marks
        students = [
            StudentMarks("Talha", [85, 90, 78]),
            StudentMarks("Raisa", [92, 88, 95]),
            StudentMarks("Sakib", [70, 75, 80]),
            StudentMarks("Sadiq", [60, 65, 55]),
            StudentMarks("Munna", [45, 50, 40])
        ]

        # printing the results for each student
        for student in students:
            student.all_results()
            print()