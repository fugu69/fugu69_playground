import os

file_path = './log.txt'

try:
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File successfully removed!")
    else:
        print("File not found")
except Exception as e:
    print(f"Error while deleting file: {e}")
