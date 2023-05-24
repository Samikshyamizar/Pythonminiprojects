class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.subjects = []
        self.grades = []
        self.total_marks = 0
        
        num_subjects = int(input("Enter the number of subjects: "))
        for i in range(num_subjects):
            subject = input(f"Enter subject {i+1}: ")
            grade = int(input(f"Enter grade for {subject}: "))
            self.subjects.append(subject)
            self.grades.append(grade)
            self.total_marks += grade
        
    def calculate_percentage(self):
        return self.total_marks / len(self.subjects)
        
    def get_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C+"
        elif percentage >= 40:
            return "C"
        else:
            return "Fail"
        
student = Student()

print(f"Name: {student.name}")
print("Subject-wise grades:")
for i in range(len(student.subjects)):
    print(f"{student.subjects[i]}: {student.grades[i]}")
    
percentage = student.calculate_percentage()
print(f"Percentage: {percentage:.2f}%")

grade = student.get_grade()
print(f"Grade: {grade}")
