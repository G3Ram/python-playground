# Bubble sort
num_list = [8, 10, 6, 2, 4]
print("Unsorted list is ", num_list)
swapped = True

count = 0

while swapped:
    swapped = False
    for i in range(len(num_list) - 1):
        count += 1
        if num_list[i] > num_list[i + 1]:
            swapped = True
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

print("Sorted list is ", num_list)
print("Number of iterations = ", count)
