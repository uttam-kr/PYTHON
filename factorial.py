def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);


num = int(input("Enter number for factorial:-"))
print("factorial of num", num, "is",
factorial(num))

