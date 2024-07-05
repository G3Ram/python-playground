# Find leap year
year = int(input("Enter year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("It's a common year")
elif year % 100 != 0:
    print("It's a leap year")
elif year % 400 != 0:
    print("It's a common year")
else:
    print("It's a leap year")
