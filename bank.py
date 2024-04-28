class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0

    def generate_account_number(self):
        return 1234 

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_taken += amount
            self.balance += amount
            self.transaction_history.append(f"Loan taken: {amount}")
            self.loan_count += 1
        else:
            print("You have already taken the maximum number of loans.")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Insufficient funds to transfer.")
        else:
            recipient_account.deposit(amount)
            self.balance -= amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient_account.name}")


class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.users.append(new_user)
        print("Account create successfully.")

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account delete successfully.")
                return
        print("Account not found.")

    def show_all_accounts(self):
        print("User Accounts:")
        for user in self.users:
            print(f"Name: {user.name}, Email: {user.email}, Account Type: {user.account_type}, Balance: {user.balance}")

    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print("Total available balance in the bank:", total_balance)

    def total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.users)
        print("Total loan amount in the bank:", total_loan)

    def toggle_loan_feature(self, status):
        if status.lower() == 'on':
            for user in self.users:
                user.loan_count = 0
            print("Loan feature is now turned on.")
        elif status.lower() == 'off':
            print("Loan feature is now turned off.")
        else:
            print("Invalid status. Please provide 'on' or 'off'.")


admin = Admin()


while True:
    print("\n1. Create Account")
    print("2. Delete Account")
    print("3. Show All Accounts")
    print("4. Check Total Available Balance")
    print("5. Check Total Loan Amount")
    print("6. Toggle Loan Feature")
    print("7. Deposit Amount")
    print("8. Withdraw Amount")
    print("9. Check Balance")
    print("10. Check Transaction History")
    print("11. Take Loan")
    print("12. Transfer Money")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        account_type = input("Enter account type (Savings/Current): ")
        admin.create_account(name, email, address, account_type)

    elif choice == "2":  
        account_number = int(input("Enter account number to delete: "))
        admin.delete_account(account_number)

    elif choice == "3":  
        admin.show_all_accounts()

    elif choice == "4":  
        admin.total_available_balance()

    elif choice == "5":  
        admin.total_loan_amount()

    elif choice == "6":  
        status = input("Enter 'on' to enable or 'off' to disable loan feature: ")
        admin.toggle_loan_feature(status)

    elif choice == "7":  
        account_number = int(input("Enter account number to deposit money: "))
        amount = float(input("Enter amount to deposit: "))
        for user in admin.users:
            if user.account_number == account_number:
                user.deposit(amount)
                print("Amount deposited successfully.")
                break
        else:
            print("Account not found.")

    elif choice == "8":  
        account_number = int(input("Enter account number to withdraw money: "))
        amount = float(input("Enter amount to withdraw: "))
        for user in admin.users:
            if user.account_number == account_number:
                if amount > user.balance:
                    print("Withdrawal amount exceeded")
                else:
                    user.withdraw(amount)
                    print("Amount withdrawn successfully.")
                break
        else:
            print("Account not found.")

    elif choice == "9":  
        account_number = int(input("Enter account number to check balance: "))
        for user in admin.users:
            if user.account_number == account_number:
                print("Balance:", user.check_balance())
                break
        else:
            print("Account not found.")

    elif choice == "10":
        account_number = int(input("Enter account number to check transaction history: "))
        for user in admin.users:
            if user.account_number == account_number:
                print("Transaction History:", user.check_transaction_history())
                break
        else:
            print("Account not found.")

    elif choice == "11":  
        account_number = int(input("Enter account number to take loan: "))
        amount = float(input("Enter loan amount: "))
        for user in admin.users:
            if user.account_number == account_number:
                user.take_loan(amount)
                print("Loan taken successfully.")
                break
        else:
            print("Account not found.")

    elif choice == "12":  
        from_account_number = int(input("Enter account number to transfer money from: "))
        to_account_number = int(input("Enter account number to transfer money to: "))
        amount = float(input("Enter amount to transfer: "))
        from_user = None
        to_user = None
        for user in admin.users:
            if user.account_number == from_account_number:
                from_user = user
            elif user.account_number == to_account_number:
                to_user = user
        if from_user and to_user:
            from_user.transfer(amount, to_user)
            print("Amount transferred successfully.")
