input("wsjdf;lsdjfl;j")

def cretAcc():
    ID=input("Please Input ID: ")
    Name=input("please Input Name: ")
    Sex=input("Please Input Sex (M/F): ")
    Dob=input("Please input Dob : ")
    Balan=float(input("Input Balan: $ "))
    with open("Deta_stor.txt","a") as deta_file:
        deta=deta_file.write(f"\n{ID}\n{Name}\n{Sex}\n{Dob}\n{Balan}")
    print("Account created successfully!\n")

def saech1():
    
    search_Id = input("Please Input Id: ").strip()
    found = False

    # អាន File ទាំងមូលមកជា String តែមួយ
    with open("Deta_stor.txt", "r") as deta_file:
        content = deta_file.read()

        # បំបែក String នោះជា List តាមបន្ទាត់ ដើម្បីងាយស្រួលអានតគ្នាបន្តបន្ទាប់
        lines = content.splitlines()

        for i in range(len(lines)):
            current_id = lines[i].strip()

            if current_id == search_Id:
                found = True
                print("\n" + "=" * 30)
                print("      ACCOUNT INFORMATION     ")
                print("=" * 30)
                print(f"  ID       : {current_id}")
                print(f"  Name     : {lines[i+1].strip()}")
                print(f"  Sex      : {lines[i+2].strip()}")
                print(f"  Dob      : {lines[i+3].strip()}")
                print(f"  Balance  : ${lines[i+4].strip()}")
                print("=" * 30 + "\n")
                break

    if not found:
        print("\n[!] Error: ID not found!\n")
2

def sowAll():

    try:
        with open("Deta_stor.txt", "r") as deta_file:
            content = deta_file.read()

            lines = [line.strip() for line in content.splitlines() if line.strip()]

            if not lines:
                print("\n not foun!\n")
                return

            print("\n" + "=" * 40)
            print("          ALL ACCOUNTS LIST          ")
            print("=" * 40)
            for i in range(0, len(lines), 5):
                if i + 4 < len(lines):
                    print(f"  ID       : {lines[i]}")
                    print(f"  Name     : {lines[i+1]}")
                    print(f"  Sex      : {lines[i+2]}")
                    print(f"  Dob      : {lines[i+3]}")
                    print(f"  Balance  : ${lines[i+4]}")
                    print("-" * 40)

    except FileNotFoundError:
        print("Account Not Fount!")


def deposit():
    search_id = input("Please input your ID for Deposit: ").strip()
    found = False

    try:
        with open("Deta_stor.txt", "r") as deta_file:
            lines = deta_file.readlines()

        for i in range(0, len(lines) - 4, 5):
            if lines[i].strip() == search_id:
                found = True
                try:
                    amount = float(input("Enter amount to deposit: $ "))
                    if amount <= 0:
                        print("Amount must be greater than 0.\n")
                        return
                    
                    current_balan = float(lines[i+4].strip())
                    new_balan = current_balan + amount
                    lines[i+4] = f"{new_balan}\n"
                    
                    # សរសេរទិន្នន័យដែលបានកែប្រែរួចចូល File វិញ
                    with open("Deta_stor.txt", "w") as deta_file:
                        deta_file.writelines(lines)
                        
                    print(f"Successfully deposited ${amount}. New Balance: ${new_balan}\n")
                except ValueError:
                    print("Invalid amount entered.\n")
                break

        if not found:
            print("\nAccount not found.\n")

    except FileNotFoundError:
        print("\nNo account records file found yet.\n")


def withdraw():
    search_id = input("Please input your ID for Withdrawal: ").strip()
    found = False

    try:
        with open("Deta_stor.txt", "r") as deta_file:
            lines = deta_file.readlines()

        for i in range(0, len(lines) - 4, 5):
            if lines[i].strip() == search_id:
                found = True
                try:
                    amount = float(input("Enter amount to withdraw: $ "))
                    if amount <= 0:
                        print("Amount must be greater than 0.\n")
                        return
                    
                    current_balan = float(lines[i+4].strip())
                    
                    if amount > current_balan:
                        print(f"Insufficient balance! Current Balance is ${current_balan}\n")
                        return
                    
                    new_balan = current_balan - amount
                    lines[i+4] = f"{new_balan}\n"
                    
                    # សរសេរទិន្នន័យដែលបានកែប្រែរួចចូល File វិញ
                    with open("Deta_stor.txt", "w") as deta_file:
                        deta_file.writelines(lines)
                        
                    print(f"Successfully withdrew ${amount}. New Balance: ${new_balan}\n")
                except ValueError:
                    print("Invalid amount entered.\n")
                break

        if not found:
            print("\nAccount not found.\n")

    except FileNotFoundError:
        print("\nNo account records file found yet.\n")

def transfer():
    sender_id = input("Please input your ID (Sender): ").strip()
    receiver_id = input("Please input target ID (Receiver): ").strip()

    if sender_id == receiver_id:
        print("You cannot transfer money to your own account.\n")
        return

    try:
        with open("Deta_stor.txt", "r") as deta_file:
            lines = deta_file.readlines()

        sender_idx = -1
        receiver_idx = -1

        # ស្វែងរកទីតាំង Balance របស់អ្នកផ្ញើ និងអ្នកទទួល
        for i in range(0, len(lines) - 4, 5):
            if lines[i].strip() == sender_id:
                sender_idx = i + 4
            elif lines[i].strip() == receiver_id:
                receiver_idx = i + 4

        if sender_idx == -1:
            print("\nSender account not found.\n")
            return
        if receiver_idx == -1:
            print("\nReceiver account not found.\n")
            return

        try:
            amount = float(input("Enter amount to transfer: $ "))
            if amount <= 0:
                print("Amount must be greater than 0.\n")
                return

            sender_balance = float(lines[sender_idx].strip())
            
            if amount > sender_balance:
                print(f"Insufficient balance! Current Balance is ${sender_balance}\n")
                return

            receiver_balance = float(lines[receiver_idx].strip())

            # កាត់លុយអ្នកផ្ញើ និង បន្ថែមលុយអ្នកទទួល
            new_sender_balance = sender_balance - amount
            new_receiver_balance = receiver_balance + amount

            lines[sender_idx] = f"{new_sender_balance}\n"
            lines[receiver_idx] = f"{new_receiver_balance}\n"

            # រក្សាទុកទិន្នន័យចូល File វិញ
            with open("Deta_stor.txt", "w") as deta_file:
                deta_file.writelines(lines)

            print(f"Successfully transferred ${amount} to Account ID: {receiver_id}")
            print(f"Your New Balance: ${new_sender_balance}\n")

        except ValueError:
            print("Invalid amount entered.\n")

    except FileNotFoundError:
        print("\nNo account records file found yet.\n")
while True:
    print("---> Welcom to Bank <---")
    print("[1]: cretAcc ")
    print("[2]: Search Account")
    print("[3]: SowAll")
    print("[4]: Diposit")
    print("[5]: withdawel")
    print("[6]: transfer")
    print("[0]: Back")
    option=int(input("plaese input your Optin: "))
    match option:
        case 1:
            cretAcc()
        case 2:
            saech1()
        case 3:
            sowAll()
        case 4:
            deposit()
        case 5:
            withdraw()
        case 6:
            transfer()

        case 0:
            break
        case _:
            print("Invalid Option")
            print("Please Input Try again : ")