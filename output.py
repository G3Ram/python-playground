# What is the output of the following snippet?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    print(my_list[v])
    my_list.insert(1, my_list[v])
    print(my_list)
print(my_list)

var = 1
while var < 10:
    print("#")
    var = var << 1


lst = [[x for x in range(3)] for i in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

lst = [i for i in range(-1, -2)]
print(lst)

x = int(input())
y = int(input())
x = x % y
print(x, y)
x = x % y
print(x, y)
y = y % x
print(y)

a = 1
b = 0
a = a ^ b
print(a, b)
b = a ^ b
print(a, b)
a = a ^ b
print(a, b)

my_lst = [1, 2]
for v in range(2):
    my_lst.insert(-1, my_lst[v])

print(my_lst)
