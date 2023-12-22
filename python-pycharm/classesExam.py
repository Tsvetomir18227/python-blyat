# klas prepodavatel - rechnik v koito kluch e fakNumber na student a value e ocenka na studenta v klasa student - poletio fakNumber
# v klasa prepodavatel - metod add_student s kluch fakNumber i stoinost 0
# oshte edin metod - set_grade kkoito po fakNumber na student postavq ocenka na suotvetniq student
# predefinirane v klasa prepodavatel print_info taka che da otpechatva i studentite na prepodavatelq s tehnite ocenki
# da se dobavi kum klasa na prepodavatelq metod average grade koito izchislqva sredniq uspeh na ocenkite na prepodavatelq i se printirat



class Person:
    def __init__(self, fname, lname, nationality, age):
        self.firstname = fname
        self.lastname = lname
        self.nationality = nationality
        self.age = age

    def print_info(self):
        print(f"Name: {self.firstname} {self.lastname}, nationality: {self.nationality}", end = "")

class Student(Person):
    def __init__(self, fname, lname, nationality, age, university, year, fakNum, grade):
        super().__init__(fname, lname, nationality, age)
        self.university = university
        self.year = year
        self.fakNum = fakNum
        self.grade = grade

class Teacher(Person):
    def __init__(self,fname,lname,nationality,age,university,year,grade):
        super().__init__(fname,lname,nationality,age)
        self.university = university
        self.year = year
        self.grade = grade
        self.student_grades = {}
        self.student_add = {}

    def add_student(self, student):
        self.student_add[student.fakNum] = 0

    def set_grade(self, fakNum, grade):
        # Add or update a grade for a student using their faculty number
        self.student_grades[fakNum] = grade

    def print_info(self):
        super().print_info()
        print(f"Uni:{self.university}, Grade: {self.grade}")



