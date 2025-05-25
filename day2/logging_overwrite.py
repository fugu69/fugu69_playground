import os

file_path = './log.txt'

with open(file_path, 'w+') as f:
    f.write("The content is overwriten")
    f.seek(0)
    print(f.read())
