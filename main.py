print("Welcome to the calculator")

num1 = float(input("Please provide the first number: "))
num2 = float(input("Please provide the second number: "))
operation = input("What operation would you like to use? addition(+), subtraction(-), multiplication(*), division(/): ")

if operation == "+": 
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation")


print("The answer is: ", result)