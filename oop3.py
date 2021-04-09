class Student:
    

    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z


    def display(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

s1= Student("Ashish",21,88)
s1.display()
s2= Student("Ash",22,90)
s2.display()