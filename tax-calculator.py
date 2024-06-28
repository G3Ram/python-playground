# Tax calculator
income = float(input("Enter your income: "))
tax = 0
if income < 85528:
    tax = (income * 18) / 100 - 556.2

print("Tax is ", tax)
