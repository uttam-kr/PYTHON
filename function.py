def greet():
    print("Hello")
    print("Have a nice day")

def sum(x,y):
    c = x + y
    print(c)
#Return single value
def sub(a,b):
    d = a - b
    return d

#Return two value
def sub_add(m,n):
    p = m - n
    q = m + n
    return p,q


greet()
sum(5,4)
result = sub(6,2)
print(result)
res1,res2 = sub_add(10,6)
print(res1,res2)
