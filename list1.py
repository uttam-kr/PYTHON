# Python program to swap first and last element of a list
newList = []
n = int(input("Enter number of element in list: "))
for i in range(0,n):
    ele = int(input("please enter number "))
    newList.append(ele)
# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


print(swapList(newList))