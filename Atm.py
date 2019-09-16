#!/usr/bin/python
import math

savingamount = input("Amount you want to deposit. Please enter in digit: ")
print("you deposited: " +str(savingamount))
withdrawamount = input("Amount you want to withdraw: ")
if int(withdrawamount) > int(savingamount):
	print("insufficient balance")
else:
	savingamount = int(savingamount) - int(withdrawamount)
	print("Your account balance: " + str(savingamount))
	print("Have a nice day!")
	
	74679

	def max(a):     
	 res = a[0] for i in array: 
	 if res < i:             
	 	res = i     
	 	return res  
	 	array = (1, 2, 3, 4, 5, 6) 
	 	print(max(array))