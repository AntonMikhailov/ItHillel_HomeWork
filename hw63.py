number = int(input("Enter a number: "))

result = number # when input number < 9
while number > 9:
    result = 1
    for digit in str(number):
        result *= int(digit)
    number = result

print(result)

# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1