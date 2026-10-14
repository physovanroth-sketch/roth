accounts = 0

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

    print("Account created successfully!")


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
