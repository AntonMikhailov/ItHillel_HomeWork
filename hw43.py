import random

random_list = [random.randint(1, 9) for _ in range(random.randint(3, 10))]
print("random_list:", random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]
print("new_list:", new_list)