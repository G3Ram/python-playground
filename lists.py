# Python lists

# Example 1 - Let's assign a new value of 111 to the first element in the list. We do it this way:
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

# Example 2 - the value of the fifth element to be copied to the second element
numbers[1] = numbers[4]
print("New list content: ", numbers)  # Current list content.

# Example 3 - Get the length of the list
print("List length : ", len(numbers))

# Example 4 - Removing numbers from a list
del numbers[4]
print("New list content after delete: ", numbers)  # Current list content.

# Example 5 - Using negative indices
print("Original list content:", numbers)
print("Negative index -1 : ", numbers[-1])
print("Negative index -2 : ", numbers[-2])

# Example 6 - append values
numbers.append(4)
print("New list content after append: ", numbers)

# Example 7 - insert values
numbers.insert(0, 444)
print("New list content after append: ", numbers)

# Example 8 - input numbers from 1 to 6 in reverse order
new_list = []
for i in range(6):
    new_list.insert(0, i + 1)

print("New list with values is : ", new_list)
