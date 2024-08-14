# tuple examples
my_tuple = (1, 23, 450, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-1:])
print(my_tuple[1:])
print(my_tuple[1:2])

for item in my_tuple:
    print(item)

# Example 2
tuple_1 = my_tuple * 2
print(tuple_1)
tuple_2 = my_tuple + (1000, 20000)
print(tuple_2)
print(1000 in my_tuple)

# Example 3
var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print("t1, t2, t3 is ", t1, t2, t3)
