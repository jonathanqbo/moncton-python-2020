# create empty dict
dict_empty = {}
print(type(dict_empty))

dict_empty2 = dict()

# create dict
dict0 = {'ranran':'be a superman',
         'jerry': 'be a billionaire',
         'zijun': 'save world'}

# create dict using keyword params. same with above
dict0 = dict(ranran='be a superman', jerry='be a billionaire', zijun='save world')

# get value by key
print(dict0['ranran'])

# add more kv
dict0['zixie'] = 'live in Mars'
dict0.update(zixie='live in sun')
dict0.update({'zixie': 'live in Mars'})

# add another dicts
dict1 = {'jiaze': 'be a super star',
         'andy': 'win Nobel Prize'}

dict0.update(dict1)

# loop keys
for key in dict0.keys():
    print(key)

for key in dict0:
    print(key)

# loop values
for value in dict0.values():
    print(value)

# loop k-v
for key, value in dict0.items():
    print(key, value)

# delete use del
del dict0['andy']
print(dict0)

# delete use pop
dict0.pop('jiaze')
print(dict0)

# contains
print('ranran' in dict0)
print('andy' not in dict0)
print('andy' in dict0)

