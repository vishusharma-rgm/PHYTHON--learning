my_tuple =(10,20,30,40,50)
print("Original Tuple:", my_tuple)
print("Type of my_tuple:", type(my_tuple))
# This code creates a tuple 'my_tuple' with five integer elements and prints the tuple along with its type.
# Output:
# Original Tuple: (10, 20, 30, 40, 50)
# Type of my_tuple: <class 'tuple'>

print("Accessing elements:")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
# This code accesses and prints the first and last elements of the tuple using indexing.
# Output:
# Accessing elements:
# First element: 10
# Last element: 50

print("Slicing the tuple:")
print("Elements from index 1 to 3:", my_tuple[1:4])
# This code slices the tuple to get elements from index 1 to 3 and prints them.
# Output:   
# Slicing the tuple:
# Elements from index 1 to 3: (20, 30, 40)

print("Iterating through the tuple:")
for item in my_tuple:
    print(item)
# This code iterates through each element in the tuple and prints it.
# Output:
# Iterating through the tuple:
# 10
# 20
# 30
# 40
# 50

# Note: Tuples are immutable, so we cannot change, add, or remove elements like we do with lists.       
print("Length of the tuple:", len(my_tuple))
# This code prints the length of the tuple using the len() function.
# Output:
# Length of the tuple: 5    


print("Concatenating tuples:")
new_tuple = my_tuple + (60, 70, 80)
print("New Tuple after concatenation:", new_tuple)
# This code concatenates a new tuple (60, 70, 80) to the existing tuple and prints the new tuple.
# Output:
# Concatenating tuples:
# New Tuple after concatenation: (10, 20, 30, 40, 50, 60, 70, 80)


print("Repeating the tuple:")
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)
# This code repeats the original tuple twice and prints the resulting tuple.
# Output:
# Repeating the tuple:
# Repeated Tuple: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

           