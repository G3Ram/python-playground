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
