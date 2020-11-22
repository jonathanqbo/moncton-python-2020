with open('file_to_override.txt', 'w') as file:
    file.write('I override whole file')


with open('file_to_append.txt', 'a') as file:
    file.write('I append to the end of file\n')

