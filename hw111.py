def prime_generator(end):
    num = 2
    while num <= end:
        sq = math.ceil(num ** 1 / 2)
        for i in range(2, sq + 1):
            if (num % i) == 0:
                break
        else:
            yield num
        num += 1


from inspect import isgenerator
import math

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
