
import json
accounts = {}

def create_account():
    
    acc_id = input("Enter your Account ID: ")

    if acc_id in accounts:
        print("Account ID already exists")
        return

    name = input("Enter your Name: ")
    sex = input("Enter your Sex : ")
    dob = input("Enter your Dob : ")
    balance = float(input("Enter Initial Balance: "))

    if balance < 0:
        print("Balance cannot be negative")
        return

    accounts[acc_id] = {
        "name": name,
        "sex" : sex ,
        "dob" : dob ,
        "balance": balance

    }
    save_data()
    print("Account created successfully")


def search_account():
    acc_id = input("Enter your Account ID: ")

    if acc_id in accounts:
        print("Name:", accounts[acc_id]["name"])
        print("Sex:",accounts[acc_id]["sex"])
        print("Dob:",accounts[acc_id]["dob"])
        print("Balance:", accounts[acc_id]["balance"])
       
    else:
        print("Account not found")
def deposit_money():
    acc_id = input("Enter your Account ID: ")

    if acc_id in accounts:
        amount = float(input("Enter your Amount: "))

        if amount > 0:
            accounts[acc_id]["balance"] += amount
            save_data()
            print("Deposit successful!")
        else:
            print("Amount must be greater than 0")
    else:
        print("Account not found")


def withdraw_money():
    acc_id = input("Enter Account ID: ")

    if acc_id in accounts:
        amount = float(input("Enter your Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > accounts[acc_id]["balance"]:
            print("Insufficient balance")
        else:
            accounts[acc_id]["balance"] -= amount
            save_data()
            print("Withdrawal successful")
    else:
        print("Account not found")


def transfer_money():
    sender = input("Enter your Sender ID: ")
    receiver = input("Enter your Receiver ID: ")

    if sender not in accounts or receiver not in accounts:
        print("Account not found!")
        return

    if sender == receiver:
        print("Cannot transfer to the same account")
        return

    amount = float(input("Enter your Amount: "))

    if amount <= 0:
        print("Amount must be greater than 0")
    elif amount > accounts[sender]["balance"]:
        print("Insufficient balance")
    else:
        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount
        save_data()
        print("Transfer successful")


def show_all_accounts():
    print("Show All Accounts")
    if not accounts:
        print("No accounts available")
        return

    for acc_id, info in accounts.items():
        print("--------------------")
        print("Account ID:", acc_id)
        print("Name:", info["name"])
        print("Sex:", info["sex"])
        print("Dob",info["dob"])
        print("Balance:", info["balance"])

def save_data():
    file = open("accounts.json", "w")
    json.dump(accounts, file)
    file.close()


def load_data():
    global accounts

    try:
        file = open("accounts.json", "r")
        accounts = json.load(file)
        file.close()
    except FileNotFoundError:
        accounts = {}




def main():

    load_data()   
    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Create Account")
        print("2. Search Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Show All Accounts")
        print("0. Exit")

        choice = input("Choose Option: ")

        match choice:
            case "1":
                create_account()
            case "2":
                search_account()
            case "3":
                deposit_money()
            case "4":
                withdraw_money()
            case "5":
                transfer_money()
            case "6":
                show_all_accounts()
            case "0":
                print("Thank you for using our Bank System")
                break
            case _:
                print("Invalid Option")
                print("Please Input Try again : ")


main()

   