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


# check function using test data
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_leap_year(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# Find the days in a month
def days_in_month(year, month):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    if month in months_30:
        return 30
    elif month in months_31:
        return 31
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
