#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 100 and 300 (both included).
list=[]
for i in range(100,301):
    if (i%7==0) and (i%5!=0):
       list.append(str(i))

print(",".join(list))