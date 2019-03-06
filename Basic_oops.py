#!/usr/bin/python
#method - function inside classes
class Employee():
	#How to initialize attribute
	#init method
	def __init__(self, employee_name, employee_age, employee_weight, employee_height):
		print('constructor called')
		#('init method or constructor called') ---->This __init__ method called constructor
		self.name = employee_name
		self.age = employee_age
		self.weight = employee_weight
		self.height = employee_height
	def Developer(self):
		print("Developer {}".format(self.name))

	def is_eligible(self):
		
		print(self.age)
		
#Variable define under __init__ method called instance variable
#An object employee1 is created using the constructor of the class Employee
employee1 = Employee("Uttam", "age 25", "65 kg", "175 cm")
#self = employee1
#Whenever we create object __init__ gets called, it create space in memory so that we can work with objects.
print(employee1.name)
print(employee1.age)
print(employee1.weight)
print(employee1.height)
print('method call')
employee1.Developer() #Method call
employee1.is_eligible()
