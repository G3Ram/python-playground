# Tax calculator
income = float(input("Enter your income: "))
tax = 0
if income < 85528:
    tax = (income * 18) / 100 - 556.2
else:
    surplus = (income - 85528) * 0.32
    tax = 14839.2 + surplus

print("Tax is ", float(round(tax)), "thalers")
