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

# lab
# Note: using + to concatenate strings lets you construct the output in a more precise way 
# than with a pure print() function, even if enriched with the end= and sep= keyword arguments.
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# lab
# replicator and concatenator - * and +
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# lab
# problem - calculate end hour and mins given start hour, mins, duration. 
# test data 1 - hour=12 mins=17 dura=59 expected output = 13:16
# test data 2 - hour=23 mins=58 dura=642 expected output = 10:40
# test data 3 - hour=0 mins=1 dura=2939 expected output = 1:0
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
dura_hour = dura // 60
dura_mins = dura % 60
end_mins = (mins + dura_mins) % 60
end_hour = (((mins + dura_mins) // 60) + hour + dura_hour) % 24
print(end_hour, end_mins, sep=":")

print(2+3*5.)

