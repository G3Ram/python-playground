def is_prime(num):
    check_prime = True
    for i in range(2, num):
        if num % i == 0:
            check_prime = False

    return check_prime


for i in range(1, 20):
    print("Is ", i, " prime? -> ", is_prime(i))
