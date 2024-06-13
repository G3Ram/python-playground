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

# scenario 12 - success
# print - multiple keyword arguments
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Monty", "Python.", end="!!\n", sep="*\n")

# Lab
# problem - Minimize the print statements
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# solution
print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****", sep="\n")

# scenario 13 - success
# print - literal
# A literal is data whose values are determined by the literal itself. You use literals to encode data and to put them into your code
print("2")
print(2)


# scenario 14 - success
# print - octal and hexadecimal numbers
# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
# The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).
print(0o123)
print(0x123)

# scenario 15 - success
# print - floating numbers
# Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals.
print(0.0000000000000000000001)

# scenario 16 - success
# print - string with quotes
# The backslash can escape quotes 
print("I like \"Monty Python\"")
print("I'm Monty Python.")
print("I\'m Monty Python.")
print('I\'m Monty Python.')

# scenario 17 - success
# print - boolean values
print(True > False)
print(True < False)

# lab
# Expected output
# "I'm"
# ""learning""
# """Python"""

# solution
print("\"I\'m\"")
print("\"\"learning\"\"")
print("\"\"\"python\"\"\"")


# scenario 18
# print - operators
# when both ** arguments are integers, the result is an integer, too.
# when at least one ** argument is a float, the result is a float, too.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)