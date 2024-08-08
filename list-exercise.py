# List Exercise/Lab
num_list = [1, 2, 3, 4, 5]
print("Original List : ", num_list)
new_num = int(input("Enter the number to replace: "))
mid_index = len(num_list) // 2
num_list[mid_index] = new_num
print("Step 1: Updated List : ", num_list)

# Step 2: Remove the last item from the list
del num_list[len(num_list) - 1]
print("Step 2: Updated List : ", num_list)

# step 3: Print the length of the existing list
print("Step 3: List length : ", len(num_list))
