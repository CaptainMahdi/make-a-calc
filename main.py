print("Welcome to the Passive Aggressive Calculator")

equation = input("Please provide the equation that you cant do by yourself: ")



if "+" in equation or "-" in equation or "*" in equation or "/" in equation:
    try:
        result = eval(equation)
        print(f'This is basic math but the answer is : {result:.2f}')
    except ZeroDivisionError:
        print("Youre trying to divide by zero, genius, that doesnt work.")
else:
    print("Thats not a real sign genius, try again")

