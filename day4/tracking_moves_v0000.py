import os
import json
import shutil

FILEPATH = './log.txt'
COUNTPATH = './count.json'

def read_count():
    try:
        if os.path.exists(COUNTPATH):
            with open(COUNTPATH, 'r+') as f:
                data = json.load(f)
                count = data.get('count', 1)
                data['count'] = count + 1
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent = 4)
            return count
        else:
            with open(COUNTPATH, 'w+') as f:
                json.dump({'count': 1}, f)
            return 1
    except Exception as e:
        print(f"Error reading or writing count: {e}")
        return 1  # safe fallback

def log_move(move):
    filepath = FILEPATH
    try:
        with open(filepath, 'a+') as f:
            f.write(move + '\n')
            f.seek(0)
            print(f.read())
    except Exception as e:
        print(f"Something went wrong: {e}")

def save_log():
    filepath = FILEPATH
    call_count = read_count()
    head, tail = os.path.split(FILEPATH)
    name, extension = os.path.splitext(tail)
    new_filepath = os.path.join(head, f"{name}_{call_count}{extension}")
    shutil.copy(filepath, new_filepath)
    
def overwrite_file():
    filepath = FILEPATH
    with open(filepath, 'w') as f:
        f.write("")
        
def confirm_exit():
    while True:
        is_save = input("Would you like to save the log of the game? (Y/N): ").lower()
        if is_save == 'n':
            return 'n'
        elif is_save == 'y':
            return 'y'
        else: 
            print("Choose a valid option.")

    
if __name__ == "__main__":
    exit_app = False

    while not exit_app:

        move = input("Enter your move:").lower()

        if move == 'exit':
            is_save = confirm_exit()
            if is_save == 'n':
                overwrite_file()
                exit_app = True
            else:
                save_log()
                overwrite_file()
                exit_app = True  
        else:
            log_move(move)
