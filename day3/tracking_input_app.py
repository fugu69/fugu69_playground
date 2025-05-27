import os
import json
# Create a log.txt if not exists
# Ask user for an input
# Store the input in the file
# exit the app
# Ask if user wants to save the log
# When app runs again check if log exists. Ask the user if they want to rename or overwrite log file
# Function to rename the file                 +
# Function to overwrite the file              +

def read_json():
    count_file = './count.json'

    try:
        if os.path.exists(count_file):                                              # Check for file existance
            with open(count_file) as f:                                             # Open the file
                data = json.load(f)                                                 # Parse data from JSON -> object {key: value}
                call_count = data.get('counter', 1)                                 #returns value of "counter" key if exists, else default value 1.
                return call_count
        else:
            with open(count_file, 'w') as f:                                        # Creates JSON file
                json.dump({'counter': 1}, f, indent=4)                              # Creates key 'counter' with value 1
                return 1
    except Exception as e:
        print(f'Something went wrong: {e}')


# TO-DO fix the issue with 'w' mode rewrites the file before reading data
def increase_json(filepath):
    count_file = './count.json'

    try:
        with open(count_file, 'r+') as f:
            data = json.load(f)
            data['counter'] = data['counter'] + 1
            f.seek(0)
            json.dump(data, f, indent = 4)
            f.truncate()
    except Exception as e:
        print(f"We met issues: {e}")

def rename():
    filepath = './log.txt'
    try:
        if os.path.exists(filepath):
            head, tail = os.path.split(filepath)
            name, ext = os.path.splitext(tail)
            call_count = read_json()
            if call_count >= 1:
                try:
                    new_path = os.path.join(head, f"{name}_{call_count}{ext}")
                    os.rename(filepath, new_path)
                    print(f"New file name is {new_path}")
                    increase_json('./count.json')
                except OSError as e:
                    print(f"Renaming failed: {e}")
    except Exception as e:
        print(f'Something went wrong: {e}')

def overwrite(filepath):
    with open(filepath, 'w') as f:
        f.write("")

def write_log(content):
    filepath = './log.txt'
    with open(filepath, 'w+') as f:
        if not content:
            f.write("Log saved but no content added.\n")  # ✅ Handles empty logs
        else:
            for i in content:
                f.write(i + '\n')


def save_log(content):
    call_count = read_json()
    filepath = './log.txt'

    if os.path.exists(filepath) and call_count >= 2:
        rename()  # ✅ Rename existing log
    write_log(content)  # ✅ Always write new log
    

content = []

while True:
    move = input("Enter your move: ").lower()

    if move == 'exit':
        while True:
            is_save = input("Would you like to save the log? (Y/N)").lower()
            if is_save in ['y', 'n']:
                break
            print("Please enter 'Y' or 'N'")

        if is_save == 'y':
            save_log(content)
        break
    else:
        content.append(move)



