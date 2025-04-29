#Write a program which can compute the factorial of a given numbers.
import pdb
pdb.set_trace()
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
x=int(input("please enter number for factorial:"))
print(fact(x))
