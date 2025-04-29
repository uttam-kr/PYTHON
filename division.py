#Write a program which will find all such numbers which are divisible by 5 but are not a multiple of 7,
#between 100 and 2014 (both included).
l=[]
for i in range(100,2014):
    if (i%5==0) and (i%7!=0):
        l.append(str(i))
print(','.join(l))

