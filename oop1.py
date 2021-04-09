class Student:

    def __init__(self):
        self.name='Ashish'
        self.age=21
        self.marks=7.46


    def talk(self):
        print("Hello, I am :",self.name)
        print("My age is",self.age)
        print("My marks are",self.marks)


s1 = Student()
s1.talk()
