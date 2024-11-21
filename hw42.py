lst = [1, 3, 5]

result = (sum(lst[i] for i in range(0, len(lst), 2))) * lst[-1] if len(lst) != 0 else 0

print(f"Result: {result}")


# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0