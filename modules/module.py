from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

# This is a sample program to understand namespace
# Here we have both pi and sin which are available from import and also from local assignment.
# We see that the initial sin and pi are printed from import
# However, the last print method uses the pi and sin from local assignment.
# This shows that local assignment takes precedence over the imported ones
