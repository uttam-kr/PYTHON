#!/usr/bin/python
#oop -How to create class
#Class keyword
#According to google style guide for python first alphabates of our class should be Capital.
#Let's create EMPLOYEE class
#In class we have attribute , method
#Attribute of EMPLOYEE can be name, age, height, weight..
#We can also define methods using attribute

class Employee():
	#How to initialize attribute
	#init method
	def __init__(self, employee_name, employee_age, employee_weight, employee_height):
		#print('init method or constructor called') ---->This __init__ method called constructor
		self.name = employee_name
		self.age = employee_age
		self.weight = employee_weight
		self.height = employee_height
#Variable define under __init__ method called instance variable
#An object employee1 is created using the constructor of the class Employee
employee1 = Employee("Uttam", "age 25", "65 kg", "175 cm")
#self = employee1
#Whenever we create object __init__ gets called, it create space in memory so that we can work with objects.
print(employee1.name)
print(employee1.age)
print(employee1.weight)
print(employee1.height)
print('<------>')
employee2 = Employee("pawan", "age 22", "60 kg", "172 cm")
print(employee2.name)
print(employee2.age)
print(employee2.weight)
print(employee2.height)

