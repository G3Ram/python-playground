# Find the largest in a list
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 31]

largest = my_list[0]
for i in my_list[1:]:
    if largest < i:
        largest = i

print("Largest in the list is ", largest)
