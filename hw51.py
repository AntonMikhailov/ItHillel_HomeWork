import string
import keyword

name = input("Enter a name for variable: ")

if (all(char == '_' for char in name) and name != '_') or name[0].isdigit() or any(char.isupper() for char in name) or any(char in string.punctuation.replace('_',' ') for char in name) or keyword.iskeyword(name):
    print(False)
else:
    print(True)


# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True