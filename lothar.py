# Lothar hypothesis
c0 = int(input("Enter a real number: "))
steps = 0
while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)

print("Steps = ", steps)

# Test Data
# 15 -> steps 17
# 16 -> steps 4
# 1023 -> steps 62
