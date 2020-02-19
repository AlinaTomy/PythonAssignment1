#Question 5: PROGRAM TO FORM A DICTIONARY FROM AN OBJECT OF A CLASS
class student(object):
    def __init__(self):
        self.name = "Alina"
        self.rollno = 4
        self.age = 23

    def do_nothing(self):
        pass

student1 = student()
print(student1.__dict__)

