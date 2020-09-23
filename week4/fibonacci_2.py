
def fibo(length):
    sequence = []

    a, b = 0, 1
    for _ in range(length):
        # append a value to the end of list
        sequence.append(a)
        a, b = b, a+b

    return sequence


print(fibo(5))


