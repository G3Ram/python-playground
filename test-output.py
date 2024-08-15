l = int([1, 2])
print(l)  # Gives a TypeError

int("python")  # ValueError

l = [1, 2, 3]
l.index(5)  # ValueError

# Note: if the step value is 0 Python raises a ValueError exception
for i in range(0, 5, 0):  # ValueError
    print(i)
