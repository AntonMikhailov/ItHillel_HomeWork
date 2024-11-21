num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the math operation (+, -, *, /): ")
result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2 if num2 !=0 else print("Error: division by zero!")
else:
    print("Error: invalid math operation")

print(f"Result: {result}")