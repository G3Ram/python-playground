# print("hiss....")

# print
# Strings, numbers, characters, logical values, objects - any of these may be successfully passed to print().
# Value returned - None. Its effect is enough.
# Scenario
# The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

# In your first lab:

# use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
# having done that, use the print() function again, but this time print your first name;
# remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
# then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
# experiment as much as you can. Change double quotes to single quotes, use multiple print() functions on the same line, and then on different lines. See what happens.

# scenario 1 - success
print("Hello! Python")

# scenario 2 - success
print("Trigger")

# scenario 3 - error
# NameError
# print(Trigger)

# scenario 4 - error
# Syntax error
# print "Trigger"

# scenario 5 - success
# Accepts both single and double quotes
print('Trigger')

# senario 6 - success
# empty print - empty line
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# senario 7 - success
# escaper character - \
# \n - new line character
print("The itsy bitsy spider \nclimbed up the waterspout.")
print()
print("Down came the rain \nand washed the spider out.")

# senario 8 - error
# escaper character - \
# SyntaxError: unterminated string literal (detected at line 52)
# To avoid this error use "\\""
# print("\")
print("\\")

# scenario 9 - success
# print - multiple arguments
# a print() function invoked with more than one argument outputs them all on one line.
# the print() function puts a space between the outputted arguments on its own initiative.
# Order of the arguments matter. First comes first printed
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

# scenario 10 - success
# print - keyword arguments
# a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
# any keyword arguments have to be put after the last positional argument (this is very important)
# The keyword argument "end" puts the content supplied at the end of whatever is printed. It does not add a space. This argument is implicit by default with the value end="\n"
print("The itsy bitsy spider" , end="who knows")
print("Monty python", end=" \n")

# scenario 11 - success
# print - keyword arguments
# a keyword argument "sep" can be used to define the seperator
print("The", "itsy", "bitsy", "spider" , sep="*", end=" ")
print("Monty python", end="!!!")
