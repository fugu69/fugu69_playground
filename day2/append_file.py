import os

file_path = './hello.txt'

if os.path.exists(file_path):
    with open(file_path, 'a+') as f:
        f.write('\nNew line added!')
        f.seek(0)
        print(f.read())
else:
    with open(file_path, 'w+') as f:
        f.write('New Hello world instance created')
        f.seek(0)
        print(f.read())
