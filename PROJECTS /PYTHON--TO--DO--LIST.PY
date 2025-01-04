tasks = []

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}'  added successfully.")
    
    
def view_tasks():
    if not tasks:
        print("no task found.")   
    else: 
        print("\nYour Tasks:")  
        for x , task in enumerate(tasks, start= 1):  
            print(f"{x}. {task}")
            
            
def Delete_task():
    view_tasks()
    if tasks: 
        try:
            task_number = int(input("Enter the task number to delete: ")) - 1    
            if 1 <= task_number < len(tasks):  
                removed_task = tasks.pop(task_number)
                print(f"Task '{removed_task}' deleted successfully.")    
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
            Delete_task()
        elif choice == "4":
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
            
            
main()            
            
            
