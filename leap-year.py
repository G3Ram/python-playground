# Find leap year
year = int(input("Enter year: "))

if year % 4 != 0:
    print("It's a common year")
elif year % 100 != 0:
    print("It's a leap year")
