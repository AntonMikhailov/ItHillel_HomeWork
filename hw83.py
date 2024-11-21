from collections import Counter

def find_unique_value(some_list):
   uniq_list = [key for key, value in Counter(some_list).items() if value == 1]
   return uniq_list[0] if len(uniq_list) > 0 else None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([5, 5, 5, 2, 2]) == None, 'Test4'
print("ОК")