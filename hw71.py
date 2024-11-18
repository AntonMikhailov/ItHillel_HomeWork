def say_hi(name, age):
  return "Hi. My name is {} and I'm {} years old".format(name.title(), age)

assert say_hi("AleX", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
