import string

input_data = input("Enter two letters(a-Z): ")

start_index = string.ascii_letters.find(input_data[0])
end_index = string.ascii_letters.find(input_data[2])

print(string.ascii_letters[start_index:end_index + 1])

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA