# scenario 1 - success
# var - simple assignment
var = 1
print(var)

# scenario 2 - success
# var - print with +
var = "3.8.5"
print("Python version: " + var)

# pythagorus theorem
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print(c)

# lab
# var - round
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# scenario 3 - success
# input - variable from input
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# scenario 4 - success
# input - input with argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# scenario 5 - error
# input - input type is always a string
# error - TypeError unsupported operand type(s) for ** or pow(): 'str' and 'float' - while trying to use it as a number
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# scenario 6 - success
# input - input type is always string so should typecast to float or int before using it for numbers
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# lab
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)