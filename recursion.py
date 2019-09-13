#factorial function using recursion
import pdb #python debugging module
def fact(n):

	if n ==0:
		return 1
	pdb.set_trace()
	return n * fact(n-1)




result = fact(5)
ptint(result)
