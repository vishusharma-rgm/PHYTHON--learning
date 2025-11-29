l1 = [1,64,23,11,22,55,89,43,78,32,56,]
l1.sort()
print(l1)
print(type(l1))
# This code sorts the list l1 in ascending order and prints the sorted list along with its type.
# Output:
# [1, 11, 22, 23, 32, 43, 55, 56, 64, 78, 89]
# <class 'list

l1.reverse()
print(l1)
# This code reverses the order of elements in the list l1 and prints the reversed list.
# Output:   
# [89, 78, 64, 56, 55, 43, 32, 23, 22, 11, 1]'>

l1.append(100)
print(l1)
# # This code appends the value 100 to the end of the list l1 and prints the updated list.
# # Output:
# # [89, 78, 64, 56, 55, 43, 32, 23, 22, 11, 1, 100]

l1.insert(3, 777)
print(l1)
# # This code inserts the value 777 at index 3 of the list l1 and prints the updated list.
# # Output:
# # [89, 78, 64, 777, 56, 55, 43, 32, 23, 22, 11, 1, 100

l1.copy()
print(l1)
# # This code creates a shallow copy of the list l1 and prints it.
# # Output:
# # [89, 78, 64, 777, 56, 55, 43, 32, 23, 22, 11, 1, 100


print(l1.pop(3))
print(l1)
# # This code removes and returns the last item from the list l1 and prints the updated list.
# # Output:
# # [89, 78, 64, 56, 55, 43, 32, 23, 22, 11, 1]