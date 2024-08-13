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


# is_leap_year using a function
def is_leap_year(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
