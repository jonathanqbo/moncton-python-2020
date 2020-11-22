try:
    with open('not_existed_file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File is not existed')
except UnicodeDecodeError as e:
    print('File is not encoded in utf-8')


try:
    with open('file_utf_16.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File is not existed')
except UnicodeDecodeError as e:
    print('File is not encoded in utf-8')


