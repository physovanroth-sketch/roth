import json

accounts = {}
FILE_NAME = "accounts.json"


# 1. Save Data
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)

    print("Data saved successfully!")


# 2. Load Data
def load_data():
    global accounts

    try:
        with open(FILE_NAME, "r") as file:
            accounts = json.load(file)

        print("Data loaded successfully!")

    except FileNotFoundError:
        accounts = {}
        print("No saved data found. Starting new system.")

    except json.JSONDecodeError:
        accounts = {}
        print("Saved file is empty or invalid.")


# 3. Create Account
def create_account():
    acc_id = input("Enter your Account ID: ")

    if acc_id in accounts:
        print("Account ID already exists")
        return

    name = input("Enter your Name: ")
    sex = input("Enter your Sex: ")
    dob = input("Enter your Dob: ")

    try:
        balance = float(input("Enter Initial Balance: "))
    except ValueError:
        print("Invalid balance")
        return

    if balance < 0:
        print("Balance cannot be negative")
        return

    accounts[acc_id] = {
        "name": name,
        "sex": sex,
        "dob": dob,
        "balance": balance
    }

    save_data()
    print("Account created successfully!")


# 4. Search Account
def search_account():
    acc_id = input("Enter your Account ID: ")

    if acc_id in accounts:
        print("\n--- Account Information ---")
        print("Account ID:", acc_id)
        print("Name:", accounts[acc_id]["name"])
        print("Sex:", accounts[acc_id]["sex"])
        print("Dob:", accounts[acc_id]["dob"])
        print("Balance:", accounts[acc_id]["balance"])
    else:
        print("Account not found")


# 5. Deposit Money
def deposit_money():
    acc_id = input("Enter your Account ID: ")

    if acc_id not in accounts:
        print("Account not found")
        return

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount")
        return

    if amount <= 0:
        print("Deposit amount must be greater than 0")
        return

    accounts[acc_id]["balance"] += amount

    save_data()

    print("Deposit successful!")
    print("Deposited:", amount)
    print("New Balance:", accounts[acc_id]["balance"])


# 6. Money Transfer
def transfer_money():
    sender_id = input("Enter your Account ID: ")

    if sender_id not in accounts:
        print("Sender account not found")
        return

    receiver_id = input("Enter receiver Account ID: ")

    if receiver_id not in accounts:
        print("Receiver account not found")
        return

    if sender_id == receiver_id:
        print("Cannot transfer to the same account")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Invalid amount")
        return

    if amount <= 0:
        print("Transfer amount must be greater than 0")
        return

    if accounts[sender_id]["balance"] < amount:
        print("Insufficient balance")
        return

    accounts[sender_id]["balance"] -= amount
    accounts[receiver_id]["balance"] += amount

    save_data()

    print("Transfer successful!")
    print("Transferred:", amount)
    print("Sender Balance:",
          accounts[sender_id]["balance"])
    print("Receiver Balance:",
          accounts[receiver_id]["balance"])


# 7. Show All Accounts
def show_all_accounts():
    if not accounts:
        print("No accounts available.")
        return

    print("\n========== ALL ACCOUNTS ==========")

    for acc_id, info in accounts.items():
        print("----------------------------------")
        print("Account ID:", acc_id)
        print("Name:", info["name"])
        print("Sex:", info["sex"])
        print("Dob:", info["dob"])
        print("Balance:", info["balance"])

    print("----------------------------------")
    print("Total Accounts:", len(accounts))


# 8. Main Menu
def main():
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Search Account")
        print("3. Deposit Money")
        print("4. Money Transfer")
        print("5. Show All Accounts")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            search_account()

        elif choice == "3":
            deposit_money()

        elif choice == "4":
            transfer_money()

        elif choice == "5":
            show_all_accounts()

        elif choice == "6":
            save_data()

        elif choice == "7":
            save_data()
            print("Thank you for using our system!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Program
load_data()
main()