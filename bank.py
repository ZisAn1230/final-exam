class Account:
    account_numbers = 1234  

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = Account.generate_account_number()  
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0

    @staticmethod
    def generate_account_number():
        Account.account_numbers += 1
        return Account.account_numbers


class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = 'off'

    def create_account(self, name, email, address, account_type):
        new_account = Account(name, email, address, account_type)
        self.accounts.append(new_account)
        print("Account created successfully with account number:", new_account.account_number)

    def delete_account(self, identifier):
        for account in self.accounts:
            if account.account_number == identifier or account.name == identifier or account.email == identifier:
                self.accounts.remove(account)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def show_users(self):
        print("User Accounts:")
        for account in self.accounts:
            print(f"Name: {account.name}, Email: {account.email}, Account Type: {account.account_type}, Balance: {account.balance}")

    def total_available_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts)
        print("Total available balance in the bank:", self.total_balance)

    def total_loan_amount(self):
        self.total_loan = sum(account.loan_taken for account in self.accounts)
        print("Total loan amount in the bank:", self.total_loan)

    def off_loan(self):
        self.loan_status = 'off'
        print("Loan feature is now turned off.")

    def on_loan(self):
        self.loan_status = 'on'
        print("Loan feature is now turned on.")

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += amount
                account.transaction_history.append(f"Deposited: {amount}")
                print("Amount deposited successfully.")
                return
        print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                if amount > account.balance:
                    print("Withdrawal amount exceeded")
                else:
                    account.balance -= amount
                    account.transaction_history.append(f"Withdrew: {amount}")
                    print("Amount withdrawn successfully.")
                    return
        print("Account not found.")

    def check_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print("Balance:", account.balance)
                return
        print("Account not found.")

    def check_transaction_history(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print("Transaction History:", account.transaction_history)
                return
        print("Account not found.")

    def take_loan(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                if account.loan_count < 2:
                    account.loan_taken += amount
                    account.balance += amount
                    account.transaction_history.append(f"Loan taken: {amount}")
                    account.loan_count += 1
                    print("Loan taken successfully.")
                    return
                else:
                    print("You have already taken the maximum number of loans.")
                    return
        print("Account not found.")

    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None
        for account in self.accounts:
            if account.account_number == from_account_number:
                from_account = account
            elif account.account_number == to_account_number:
                to_account = account
        if from_account and to_account:
            if amount > from_account.balance:
                print("Insufficient funds to transfer.")
            else:
                to_account.balance += amount
                from_account.balance -= amount
                from_account.transaction_history.append(f"Transferred: {amount} to {to_account.name}")
                to_account.transaction_history.append(f"Received: {amount} from {from_account.name}")
                print("Amount transferred successfully.")
        else:
            print("One or both of the accounts not found.")


bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Delete Account")
    print("3. Show All Accounts")
    print("4. Check Total Available Balance")
    print("5. Check Total Loan Amount")
    print("6. Toggle Loan Feature (On/Off)")
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
        bank.create_account(name, email, address, account_type)

    elif choice == "2":  
        identifier = input("Enter account number, name, or email to delete: ")
        bank.delete_account(identifier)

    elif choice == "3":  
        bank.show_users()

    elif choice == "4":  
        bank.total_available_balance()

    elif choice == "5":  
        bank.total_loan_amount()

    elif choice == "6":  
        status = input("Enter 'on' to enable or 'off' to disable loan feature: ")
        if status.lower() == 'on':
            bank.on_loan()
        elif status.lower() == 'off':
            bank.off_loan()
        else:
            print("Invalid status. Please provide 'on' or 'off'.")

    elif choice == "7":  
        account_number = int(input("Enter account number to deposit money: "))
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)

    elif choice == "8":  
        account_number = int(input("Enter account number to withdraw money: "))
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)

    elif choice == "9":  
        account_number = int(input("Enter account number to check balance: "))
        bank.check_balance(account_number)

    elif choice == "10":
        account_number = int(input("Enter account number to check transaction history: "))
        bank.check_transaction_history(account_number)

    elif choice == "11":  
        account_number = int(input("Enter account number to take loan: "))
        amount = float(input("Enter loan amount: "))
        bank.take_loan(account_number, amount)

    elif choice == "12":  
        from_account_number = int(input("Enter account number to transfer money from: "))
        to_account_number = int(input("Enter account number to transfer money to: "))
        amount = float(input("Enter amount to transfer: "))
        bank.transfer_money(from_account_number, to_account_number, amount)

    elif choice == "13":  
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
