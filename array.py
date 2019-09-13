#!/usr/bin/python

from array import *

arr = array('i',[])

n = int(input("Enter the length of array: "))


for i in range(n):
	x = int(input("Enter the next value: "))
	arr.append(x)

print(arr)

val = int(input("Enter the number for search index value: "))
k = 0

for e in arr:
	if e==val:
		print(k)
		break

	k+=1

 
