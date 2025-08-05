print("Just Calculator")

choose = input("Enter Operator (+, -, *, /, ^2 for square, √ or sqrt for root): ")

if choose in ["+", "-", "*", "/"]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choose == "+":
        result = num1 + num2
    elif choose == "-":
        result = num1 - num2
    elif choose == "*":
        result = num1 * num2
    elif choose == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    print("Result:", result)
    
elif choose == "^2":
    num = float(input("Enter a number: "))
    result = num ** 2
    print("Square:", result)

elif choose in ["√", "sqrt"]:
    num = float(input("Enter a number: "))
    result = num ** 0.5
    print("Square Root:", result)

else:
    print("INVALID CHOICE MAN!!")
