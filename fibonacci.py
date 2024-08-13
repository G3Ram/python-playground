# find the Fibonacci value
def fib(n):
    if n < 1:
        return
    if n == 1 or n == 2:
        return 1
    base_val = [1, 1]
    for i in range(2, n):
        base_val.append(base_val[i - 1] + base_val[i - 2])

    return base_val[n - 1]


for j in range(1, 10):
    print("Fib value of ", j, "is : ", fib(j))
