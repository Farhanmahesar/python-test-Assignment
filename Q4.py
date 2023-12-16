people = int(input("Enter the number of people: "))
meal = float(input("Enter the cost of each meal: "))
tax = float(input("Enter the sales tax percentage: "))
tip = float(input("Enter the tip percentage: "))
food = people * meal
sales_tax = food * tax / 100
tip_amount = food * tip / 100
bill = food + sales_tax + tip_amount
bill_per_person = bill / people
print("Total cost of food:", food)
print("Total sales tax:", sales_tax)
print("Total tip amount:", tip_amount)
print("Total bill amount:", bill)
print("Total bill amount per person:", bill_per_person)
