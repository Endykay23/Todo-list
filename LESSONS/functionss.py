tasks = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)  # Appends the user input to the tasks list
    print(f"'{task}' has been added to the list.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_number < len(tasks):
                removed_task = tasks.pop(task_number)
                print(f"'{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()