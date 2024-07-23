# Find the height of the blocks
number_of_blocks = int(input("Enter number of blocks: "))
height = []
while number_of_blocks > 0:
    if len(height) == 0:
        height.append(1)
        number_of_blocks -= 1
    else:
        for i in range(len(height)):
            if number_of_blocks > 0:
                height[i] += 1
                number_of_blocks -= 1
        if number_of_blocks > 0:
            height.append(1)
            number_of_blocks -= 1

print(len(height))

# Test Data
# 6 -> 3
# 20 -> 5
# 1000 -> 44
# 2 -> 1
