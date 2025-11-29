friends = ["Alice", "Bob", "Charlie", "Diana"]
for friend in friends:
    print("Hello, " + friend + "!")
# This code iterates through a list of friends and prints a greeting for each one.
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
# Hello, Diana!

friends[0] = "Eve"
print(friends)
# This code changes the first friend's name from "Alice" to "Eve" and prints the updated list.
# Output:
# ['Eve', 'Bob', 'Charlie', 'Diana']

friends.append("Frank")
print(friends)
# This code adds a new friend "Frank" to the end of the list and prints the updated list.
# Output:
# ['Eve', 'Bob', 'Charlie', 'Diana', 'Frank']

print(friends[0:3])
# This code prints the first three friends in the list using slicing.
# Output:
# ['Eve', 'Bob', 'Charlie']