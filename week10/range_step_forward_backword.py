def step_forward(ant):
    print(f'{ant} ---->')


def step_backward(ant):
    print(f'<--- {ant}')


# comprehension syntax:
# ants = ['ant'+str(i) for i in range(20)]

ants = []
for i in range(20):
    ants.append('ant' + str(i))

for i in range(0, len(ants), 2):
    step_forward(ants[i])

for i in range(1, len(ants), 2):
    step_backward(ants[i])
