# Find the factorial of n
def get_factorial(num):
    if num <= 0:
        return None
    if num == 1:
        return 1
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


n = int(input("Enter a integer value :"))
print("Factorial of ", n, "is : ", get_factorial(n))
