tasks = []

def mobile_ussd():
    while True:
        ussd = input("Enter USSD code: ")
        if ussd == "*170#":
            print("WELCOME")
            momo_menu()
            break  # Exit the loop after a successful code
        else:
            print("Invalid code. Please try again.")

def momo_menu():
    print("\nMomo Menu:")
    print("1. Transfer Money")
    print("2. Momo Pay")
    print("3. Airtime & Bundles")
    print("4. Allow Cashout")
    print("5. My Wallet")

    choice = input("Enter a Momo Menu option: ")
    if choice == "1":
        transfer_money()
    elif choice in ["2", "3", "4", "5"]:
        print(f"Option {choice} selected. Feature coming soon!")
    else:
        print("Invalid option. Please try again.")
        momo_menu()

def transfer_money():
    task = input("Enter task for Transfer Money: ")
    tasks.append(task)  # Appends the user input to the tasks list
    print(f"'{task}' has been added to the list.")

# Start the program
mobile_ussd()
