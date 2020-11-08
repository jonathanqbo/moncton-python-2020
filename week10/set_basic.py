# empty set
# empty_set = {}  # this is not working, it's empty dict
# print(type(empty_set))
empty_set = set()
print(type(empty_set))

# set from values
set0 = {1, 2, 3, 4, 3, 2, 2, 1, 6}
print(set0)

# set from tuple
set1 = set((1, 2, 3, 4, 3, 2, 2, 1, 6))
print(set1)

# set from list
set2 = set([1, 2, 3, 4, 3, 2, 2, 1, 6])
print(set2)

# add, remove
set3 = {1, 2, 3}
set3.add(4)
print(set3)

set3.remove(4)
print(set3)

# add values from another set
set3.update({4, 5, 6})
print(set3)

# contains
set4 = {'ranran', 'zijun', 'jiaze', 'fish'}
print('ranran' in set4)
print('ranran' not in set4)

# algebra
set5 = {1, 2, 3, 4, 5, 6}
set6 = {4, 5, 6, 7, 8, 9}

# in set5 but not in set6
set7 = set5 - set6
set71 = set5.difference(set6)
print(set7, set71)

# in set5 or set 6
set8 = set5 | set6
set81 = set5.union(set6)
print(set8, set81)

# in set5 and set6
set9 = set5 & set6
set91 = set5.intersection(set6)
print(set9, set91)

# in either set5 or set6, but not in both
set99 = set5 ^ set6
set991 = set5.symmetric_difference(set6)
print(set99, set991)

# subset/superset/disjoint
set10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set11 = {1, 2, 3}
set12 = {11, 12, 13}

# super set
print(set10.issuperset(set11))
print(set10 >= set11)
print(set10 > set11)

# sub set
print(set11.issubset(set10))
print(set11 <= set10)
print(set11 < set10)

# is joint
print(set12.isdisjoint(set10))

# index and slice as list/tuple is not supported in set

# loop
for value in set0:
    print(value)

