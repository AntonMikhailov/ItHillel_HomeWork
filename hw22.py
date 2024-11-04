number = input("Enter a five-digit number: ")
if len(number) == 5:
    reversed_number = number[::-1]
    print("Reversed number: ",reversed_number)
else:
    print("Error! Please enter a five-digit-number.")