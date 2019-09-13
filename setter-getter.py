class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input('Enter no of student:'))
for i in range(n):
    name=input('Enter name:')
    marks=int(input('Enter marks:'))
    s=Student()
    s.setName(name)
    s.setMarks(marks)

    print('Hi',s.getName())
    print('your marks are:',s.getMarks())
    print('='*20)