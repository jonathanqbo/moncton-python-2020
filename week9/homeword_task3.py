import random

numbers_list = []
for _ in range(100):
    numbers_list.append(random.randrange(1000))

# create tuple from list
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)

numbers_tuple_sorted = sorted(numbers_tuple, reverse=True)
for number in numbers_tuple_sorted:
    print(number)
