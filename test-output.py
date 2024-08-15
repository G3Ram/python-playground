l = int([1, 2])
print(l)  # Gives a TypeError

int("python")  # ValueError

l = [1, 2, 3]
l.index(5)  # ValueError

# Note: if the step value is 0 Python raises a ValueError exception
for i in range(0, 5, 0):  # ValueError
    print(i)

x = int(3.5)  # Removes the decimal part only. No flooring or ceiling
y = str(3)
z = float(0)

print(x, y, z)


# Try to solve the example step by step
# This example returns a tuple
def rectangle(b, h):
    perimeter = (b + h) * 2
    area = b * h
    return b, h, area, perimeter  # This returns a tuple


print(rectangle(10, 3)[2])  # The third element in the tuple should be printed

# Bitwise operator

x = 1  # This refers to -> 1 : 1 * 2 ** 0 = 1

x = x << 2  # This refers to -> 100: 1 * 2 ** 2 + 0 * 2 ** 1 + 0 * 2 ** 0

print(x)
