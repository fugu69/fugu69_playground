from os import path

file_path = './hello.txt'

if path.exists(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        print('File already exists. Content:')
        print(content)
else:
    with open(file_path, 'w+') as f:
        f.write('Hello world!')
        f.seek(0)
        content = f.read()
    print(f'File created and the content written: "{content}"')
