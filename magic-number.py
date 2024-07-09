# Find the magic number
secret_number = 777
is_secret_number = False
while not is_secret_number:
    user_input = int(input("Guess the secret number: "))
    if user_input == secret_number:
        print("Well done, muggle! You are free now.")
        is_secret_number = True
    else:
        print("Ha ha! You're stuck in my loop!")
