
nums = [2,3,4,5,6,78,89]
#Here filter will take two argument: function and list
even = list(filter(lambda n : n%2 == 0,nums))

doubles = list(map(lambda n : n*2, even))

print(doubles)

sum = reduce(lambda a,b : a+b,doubles)
print(sum)
