# Different loops
for i in range(10):
    print("The value of i is currently", i)

for j in range(2, 8):
    print("The value of j is currently", j)

for k in range(0, 10, 2):
    print("The value of k is currently", k)

# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
print("Odd numbers from 0 to 10")
for i in range(1, 11, 2):
    print(i)

x = 1
while x < 11:
    print(x)
    x += 2

# ex 5
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
