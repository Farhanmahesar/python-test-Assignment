num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 1 and num2 % 2 == 1:
    sum_of_squares = num1 ** 2 + num2 ** 2
    print("The sum of their squares is:", sum_of_squares)
else:
    print("Sorry, the calculation cannot be performed because at least one number is even.")