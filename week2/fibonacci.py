sequence = []

a, b = 0, 1
for _ in range(20):
    # append a value to the end of list
    sequence.append(a)
    a, b = b, a+b

# get value from start
print('sequence[0]', sequence[0])
print('sequence[1]', sequence[1])
print('sequence[2]', sequence[2])
print('sequence[18]', sequence[18])
print('sequence[19]', sequence[19])

# use list len to get last value
print('sequence[len(sequence)-1]', sequence[len(sequence)-1])

# get value from end
print('sequence[-1]', sequence[-1])
print('sequence[-2]', sequence[-2])
print('sequence[-3]', sequence[-3])

# first 10
print('sequence[0:10]', sequence[0:10])
print('sequence[:10]', sequence[:10])
# last 10
print('sequence[-10:]', sequence[-10:])


