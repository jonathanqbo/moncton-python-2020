# FileNotFoundError
try:
    file = open('not_existed_file.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File is not existed')
except UnicodeDecodeError as e:
    print('File is not encoded in utf-8')
    file.close()

# UnicodeDecodeError
try:
    file = open('file_utf_16.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File is not existed')
except UnicodeDecodeError as e:
    print('File is not encoded in utf-8')
    file.close()

# Success file read
try:
    file = open('file_pokemon_lyric.txt', 'r')

    # read all
    print('\n ----- read all -----\n')
    print(file.read())

    # go to the beginning of file, and read one line
    print('\n ----- read one line -----\n')
    file.seek(0)
    print(file.readline())

    # read lines - v1
    print('\n ----- read lines v1 -----\n')
    file.seek(0)
    for line in file.readlines():
        print(line)

    # read lines - v2
    print('\n ----- read lines v2 -----\n')
    file.seek(0)
    for line in file:
        print(line)

    file.close()
except FileNotFoundError:
    print('File is not existed')
except UnicodeDecodeError as e:
    print('File is not encoded in utf-8')
    file.close()


