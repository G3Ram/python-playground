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
