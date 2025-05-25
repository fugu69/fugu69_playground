import os

file_path = './log.txt'

def add_number_to_filename(filepath, number):
    try:
        if os.path.exists(file_path):
            head, tail = os.path.split(filepath)
            name, extension = os.path.splitext(tail)
            new_path = name + str(number) + extension
            os.rename(filepath, new_path)
            print(f"The file was renamed to {new_path}")
            return new_path
        else:
            with open(file_path, 'w+') as f:
                f.write("")
    except Exception as e:
        print("Somthing went wrong: {e}")
        
add_number_to_filename("./log.txt", 2)
