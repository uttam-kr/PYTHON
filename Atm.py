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
	
	