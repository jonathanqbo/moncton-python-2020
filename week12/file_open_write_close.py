try:
    file = open('file_to_override.txt', 'w')
    file.write('I override whole file\n')
    file.write('I write more\n')
    file.write('I write more and more\n')
finally:
    file.close()


try:
    file = open('file_to_append.txt', 'a')
    file.write('I append to the end of file\n')
    file.write('I write more\n')
    file.write('I write more and more\n')
finally:
    file.close()

