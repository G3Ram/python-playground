x = 2
y = 1
x *= y + 1
print(x)

num = 1


def func():
    num = num + 3
    print(num)


func()
print(num)

d1 = {1: "one", 2: "two", 3: "three"}  # line 1
# line 2
d2 = d1  # line 3
del d1  # line 4
# line 5
print(d2)

d1 = [1, 2, 3]
d2 = d1
del d1[:]
print(d2)

d = [1, 2, 3, 4, 5]
del d[:]
print(d)
del d
print(d) - NameError


def fun(a=2, b=3):
    return a * b


print(fun())
