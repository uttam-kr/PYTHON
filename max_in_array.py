#!/usr/bin/python
#define the function with a as the parameter, and call the function with array as the argument.
def max_in_list(a):
    res = a[0]
    for i in a:
        if res < i:
            res = i
    return res

array = [1, 2, 3, 4, 5, 6]
print(max_in_list(array))