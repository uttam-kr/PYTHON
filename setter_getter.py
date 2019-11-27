#!/usr/bin/python
#Hiding data bihind method
class Employee:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name 
s=Employee()
s.setName("uttam")
print("Employee name:",s.getName())

