import os

def write(content):
    file_path = './log.txt'
    with open(file_path, 'a+') as f:
        f.write('\n'+ content)
        f.seek(0)
        print(f.read())

exit = False

while not exit:
    content = input("Enter you move: ").lower()
    if content != 'exit':
        write(content)
    else:
        exit = True

            
