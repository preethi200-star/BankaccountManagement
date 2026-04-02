# Bank Account Management System (Menu-Driven)

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount!")

    def check_balance(self):
        print(f"Account [{self.account_number}] - Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            super().withdraw(amount)
        else:
            print("Savings Account: Insufficient funds!")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Current Account: Withdrawal exceeds overdraft limit!")


# ------------------------------
# Menu-Driven Program
# ------------------------------

accounts = {}  # store accounts by account_number

def create_account():
    acc_num = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (savings/current): ").lower()
    deposit = float(input("Enter Initial Deposit: "))

    if acc_type == "savings":
        accounts[acc_num] = SavingsAccount(acc_num, name, deposit)
    elif acc_type == "current":
        accounts[acc_num] = CurrentAccount(acc_num, name, deposit)
    else:
        print("Invalid account type!")
        return

    print(f"{acc_type.capitalize()} Account created successfully for {name}!")


def access_account():
    acc_num = int(input("Enter Account Number: "))
    if acc_num not in accounts:
        print("Account not found!")
        return

    account = accounts[acc_num]

    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n=== Bank Account Management System ===")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            access_account()
        elif choice == "3":
            print("Thank you for using the Bank Account Management System!")
            break
        else:
            print("Invalid choice!")


# Run program
main()
