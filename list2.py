# Python program to remove Nth word in given list

# Function to remove Ith word
def RemoveWord(list, word, N):
    count = 0

    for i in range(0, len(list)):
        if (list[i] == word):
            count = count + 1

            if (count == N):
                del (list[i])
                return True

    return False


# Driver code
list = ['uttam', 'kumar', 'uttam']
word = 'uttam'
N = 2

result = RemoveWord(list, word, N)

if (result == True):
    print("Updated list is: ", list)
else:
    print("Item not Updated")