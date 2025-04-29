#Python program to find largest number in a list
#Creating empty list
list = []
#Asking no of element to put in list
num = int(input("Enter number of element in list:"))

#iterating through no to append element in list
for i in range(1, num+1):
    ele = int(input("Enter element: "))
    list.append(ele)

#print max no
print("Largest element is:", max(list))




