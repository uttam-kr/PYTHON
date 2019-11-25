#!/usr/bin/python
class Employee:
    '''This class is developed by uttam for demo purpose'''
    #print(Employee.__doc__)
    #__doc__ string is used to get class information.
    #help(Employee)
    def __init__(self,eno,ename,esal,eaddr):
        #self:- self is a refrence variable which is always pointing to current object. within the python class to refer current object we should use self variable.
        #1st argument of init method/constructor and instance method should be self.
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print('*'*20)
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)

e1=Employee(5,'uttam',50000,'bangalore')
e2=Employee(6,'Kumar',60000,'bangalore')

e1.info()
e2.info()
