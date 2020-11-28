data_file = 'game_history.txt'

while True:
    try:
        inputs = input('\nGive date and duration of your game playing (give "q" to stop):')
        if inputs == 'q':
            break

        date, duration = inputs.split()
        duration = int(duration)

        with open(data_file, 'a') as file:
            file.write(f'{date} {duration}\n')
            print('data saved!')

    except (IndexError, ValueError, FileNotFoundError):
        print('Wrong input! Try again\n')
        continue

try:
    print('\nYour gaming history:')
    with open(data_file, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('No history data yet')