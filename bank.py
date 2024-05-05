class User:
    account_numbers = 1234

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = User.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0

    @staticmethod
    def generate_account_number():
        User.account_numbers += 1
        return User.account_numbers

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
        print("Balance:", self.balance)

    def check_transaction_history(self):
        print("Transaction History:", self.transaction_history)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_taken += amount
            self.balance += amount
            self.transaction_history.append(f"Loan taken: {amount}")
            self.loan_count += 1
            print("Loan taken successfully.")
        else:
            print("You have already taken the maximum number of loans.")

    def transfer_money(self, to_account, amount):
        if to_account:
            if amount > self.balance:
                print("Insufficient funds to transfer.")
            else:
                to_account.deposit(amount)
                self.withdraw(amount)
                self.transaction_history.append(f"Transferred: {amount} to {to_account.name}")
                to_account.transaction_history.append(f"Received: {amount} from {self.name}")
                print("Amount transferred successfully.")
        else:
            print("Account does not exist.")


class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.users.append(new_user)
        print("Account created successfully with account number:", new_user.account_number)

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted successfully.")
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
    print("6. Toggle Loan Feature (On/Off)")
    print("7. User: Deposit Amount")
    print("8. User: Withdraw Amount")
    print("9. User: Check Balance")
    print("10. User: Check Transaction History")
    print("11. User: Take Loan")
    print("12. User: Transfer Money")
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
        user = next((user for user in admin.users if user.account_number == account_number), None)
        if user:
            user.deposit(amount)
        else:
            print("Account not found.")

    elif choice == "8":
        account_number = int(input("Enter account number to withdraw money: "))
        amount = float(input("Enter amount to withdraw: "))
        user = next((user for user in admin.users if user.account_number == account_number), None)
        if user:
            user.withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "9":
        account_number = int(input("Enter account number to check balance: "))
        user = next((user for user in admin.users if user.account_number == account_number), None)
        if user:
            user.check_balance()
        else:
            print("Account not found.")

    elif choice == "10":
        account_number = int(input("Enter account number to check transaction history: "))
        user = next((user for user in admin.users if user.account_number == account_number), None)
        if user:
            user.check_transaction_history()
        else:
            print("Account not found.")

    elif choice == "11":
        account_number = int(input("Enter account number to take loan: "))
        amount = float(input("Enter loan amount: "))
        user = next((user for user in admin.users if user.account_number == account_number), None)
        if user:
            user.take_loan(amount)
        else:
            print("Account not found.")

    elif choice == "12":
        from_account_number = int(input("Enter account number to transfer money from: "))
        to_account_number = int(input("Enter account number to transfer money to: "))
        amount = float(input("Enter amount to transfer: "))
        from_user = next((user for user in admin.users if user.account_number == from_account_number), None)
        to_user = next((user for user in admin.users if user.account_number == to_account_number), None)
        if from_user:
            from_user.transfer_money(to_user, amount)
        else:
            print("Account not found.")

    elif choice == "13":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose a valid option.")

