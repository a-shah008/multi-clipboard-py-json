import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def clear_data(filepath):
    with open(filepath, "w") as f:
        pass

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data successfully saved.")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        for item in data:
            if data[item] == "":
                print(f"\nKey: \"{item}\", Value: Undefined")
            else:
                print(f"\nKey: \"{item}\", Value: \"{data[item]}\"\n")
    elif command == "clear":
        clear_data(SAVED_DATA)
    else:
        print("Unknown command. Try again.")

else:
    print("Please type in exactly one command.")
