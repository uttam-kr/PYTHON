#!/usr/bin/python

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
#Below written method is instance method because we are using here instance variable.
    def display(self):
        print('Hi',self.name)
        print('your marks are',self.marks)
#Object related method called instance method, 1st argument should be self in instance method
    def grade(self):
        if self.marks>=60:
            print('you secured First Grade')
        elif self.marks>=50:
            print('you secured Second Grade')
        elif self.marks>=35:
            print('you secure Third Grade')
        else:
            print('you are failed')

n=int(input('Enter no of student:'))
for i in range(n):
    name=input('Enter name:')
    marks=int(input('Enter marks:'))
    s=Student(name,marks)
    s.display()
    s.grade()
    print('='*20)



