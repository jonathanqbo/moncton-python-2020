# ------ ZeroDivisionError ------

try:
    10 / 0
except ZeroDivisionError:
    print('Catch ZeroDivisionError')

try:
    10 // 0
except ZeroDivisionError:
    print('Catch ZeroDivisionError')

# ------ IndexError ------

try:
    list1 = [1, 2, 3]
    list1[8]
except IndexError:
    print('Catch IndexError')

try:
    tuple1 = (1, 2, 3)
    tuple1[8]
except IndexError:
    print('Catch IndexError')

# ------ KeyError ------

try:
    dict1 = {'key1': 'value1', 'key2': 'value2'}
    dict1['key3']
except KeyError:
    print('Catch KeyError')

# ------ AttributeError ------

try:
    list2 = []
    print(list2.dosomething())
except AttributeError:
    print('Catch AttributeError')

# ------ TypeError ------
try:
    'i am str' + 100
except TypeError:
    print('Catch TypeError')

try:
    int(None)
except TypeError:
    print('Catch TypeError')

try:
    # {1, 2, 3} + [4, 5, 6]
    {1, 2, 3} + 4
except TypeError:
    print('Catch TypeError')

# ------ ValueError ------
try:
    int('I am not valid integer number')
except ValueError:
    print('Catch ValueError')

# ------ NameError ------
try:
    if False:
        none_exist_var = 'i will never be initialized'

    print(none_exist_var)
except NameError:
    print('Catch NameException')