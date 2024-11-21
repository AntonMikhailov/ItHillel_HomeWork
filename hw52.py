while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the math operation (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: division by zero!")
            continue
        result = num1 / num2
    else:
        print("Error: invalid math operation!")
        continue
    print(f"Result: {result}")

    repeat = input("Do you want to use the calculator again? (Y/N): ").strip().lower()
    if repeat != 'y':
        break