seconds = int(input("Enter the number of seconds from 0 to 8640000: "))

days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

if days % 10 == 1 and days % 100 != 11:
    print(f"{days} день, {hours:02d}:{minutes:02d}:{seconds:02d}")
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    print(f"{days} дні, {hours:02d}:{minutes:02d}:{seconds:02d}")
else:
    print(f"{days} днів, {hours:02d}:{minutes:02d}:{seconds:02d}")

# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59