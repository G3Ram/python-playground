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


# Read the question carefully
n = 4

while n > 0:
    print("#")
    n //= 2  # This is an integer division

# ValueError exception if step is 0
# Note: step should be a non-zero number
for i in range(0, 5, 0):
    print(i)

# Note: Strings in Python are immutable
s = "python"

s[0] = "P"

print(s)

# Note: 0 % n is always 0
lst1 = [0, 3, 4, 6, 30]
lst2 = []

for n in range(len(lst1)):
    if lst1[n] % 2 == 0 and lst1[n] % 3 == 0:
        lst2.append(lst1[n])

print(lst2)  # [0, 6, 30] : Make sure not to miss 0

# Note: After a break in for or while loop the else part will not get implemented
str = "Monty"

for i in str:
    print(i)
    break
else:
    print("Python")
# This will break and only print 'M'

# Note: single back slash in a string is only to have the line broken for display.
# The string as it is is still unbroken
incipit = "It was \
a dark and \
stormy night"

print(incipit)

# Note: When a dictionary is iterated using .items, the result is a tuple
test_results = {"Python": 77, "C++": 69, "Java": 81}

for i in test_results.items():
    print(i)  # This prints out a tuple with key value pair

# Note: ch will take the value of 'n'
for ch in "Python":
    pass
print(ch)

# Note: prints []
print(list(range(-3)))

# Following code throws a syntax error.
# print(03 + 4 * 2)

l = [4, 3, 1, 5, 2, 1]

# Finds the first index when 1 occurs
x = l.index(1)  # x = 2
l.remove(x)  # l.remove(x) means removing the value 2 from the list

print(l)  # [4, 3, 1, 5, 1]

# Note: Integer division floors the value
x = -5 // 4  # -1 will be rounded to -2

d = {"x": 1, "y": 2, "xy": 3, "Xy": 4}

d["xY"] = 5

print(d)  # {'x': 1,'y': 2, 'xy': 3, 'Xy': 4, 'xY': 5}

# Note: Following gives an attribute error
tpl = (1, 2, 3, 4)

tpl.append(5)

# ch will be available even after the for loop is done
for ch in "Python":
    pass

print(ch)

print(list(range(-3)))  # []
