class Person:
    def __init__(self, fname, lname, nationality, age):
        self.firstname = fname
        self.lastname = lname
        self.nationality = nationality
        self.age = age

    def print_info(self):
        print(f"Name: {self.firstname} {self.lastname}, nationality: {self.nationality}", end="")

class Student(Person):
    def __init__(self, fname, lname, nationality, age, university, year, fakNum, grade):
        super().__init__(fname, lname, nationality, age)
        self.university = university
        self.year = year
        self.fakNum = fakNum
        self.grade = grade

class Teacher(Person):
    def __init__(self, fname, lname, nationality, age, university, year, grade=0):
        super().__init__(fname, lname, nationality, age)
        self.university = university
        self.year = year
        self.grade = grade
        self.student_grades = {}
        self.student_add = {}

    def add_student(self, student):
        self.student_add[student.fakNum] = student.grade  # Use the grade from the student instance

    def set_grade(self, fakNum, grade):
        # Add or update a grade for a student using their faculty number
        self.student_grades[fakNum] = grade

    def print_info(self):
        super().print_info()
        print(f", Uni: {self.university}, Grade: {self.grade}")

# Example usage:
student1 = Student("John", "Doe", "US", 20, "ABC University", 2, "F12345", 0)
student2 = Student("Alice", "Smith", "UK", 21, "XYZ University", 3, "F67890", 0)

# Create an instance of Teacher
teacher = Teacher("Dr. Smith", "Jones", "Canada", 35, "XYZ University", 5)

# Add students to the teacher's records
teacher.add_student(student1)
teacher.add_student(student2)

# Set grades for students
student1.set_grade("F12345", 90)
student2.set_grade("F67890", 85)

# Print information for the teacher
teacher.print_info()
