import os

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print("\n--- File Contents ---")
    print(content)
    print("---------------------\n")

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' has been created and saved.\n")

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Text has been appended to '{filename}'.\n")

def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.\n")

def replace_line_in_file(filename, line_number, new_text):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text + '\n'
        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} has been replaced.\n")
    else:
        print(f"Error: The file has only {len(lines)} lines. Unable to replace line {line_number}.\n")

def main():
    filename = input("Enter the filename: ").strip()

    if os.path.exists(filename):
        print(f"\nThe file '{filename}' already exists. What would you like to do?")
        print("A) Read the file")
        print("B) Delete the file and start over")
        print("C) Append to the file")
        print("D) Replace a single line")
        choice = input("\nEnter your choice (A/B/C/D): ").strip().upper()

        if choice == "A":
            read_file(filename)
        elif choice == "B":
            delete_file(filename)
            content = input("Enter the text you want to write to the file: ")
            write_file(filename, content)
        elif choice == "C":
            content = input("Enter the text you want to append to the file: ")
            append_to_file(filename, content)
        elif choice == "D":
            line_number = int(input("Enter the line number you want to replace: "))
            new_text = input("Enter the new text for that line: ")
            replace_line_in_file(filename, line_number, new_text)
        else:
            print("Invalid choice. Exiting program.")
    else:
        content = input("File not found. Enter the text you want to write to the new file: ")
        write_file(filename, content)

if __name__ == "__main__":
    main()
