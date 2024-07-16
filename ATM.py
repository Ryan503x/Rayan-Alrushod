class NormalAccount:
    def __init__(self):
        self.balance = 5000

    def show_menu(self):
        print("---" * 15)
        print("Welcome! Select an option:")
        print("(1) Withdraw   (2) Deposit")
        print("(3) Balance    (0) Exit")
        return int(input("Choose a number: "))

    def withdraw(self, amount):
        if amount > 5000:
            print("You can't withdraw more than 5000")
        elif amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Your balance now is {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print(f"Your balance now is {self.balance}")

    def check_balance(self):
        print(f"Your account balance is {self.balance}")

    def run(self):
        while True:
            selection = self.show_menu()
            if selection == 1:
                amount = int(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif selection == 2:
                amount = int(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif selection == 3:
                self.check_balance()
            elif selection == 0:
                print("Thank you! Have a great day.")
                break
            else:
                print("Invalid input. Please choose a valid option.")

class RestrictedAccount:
    def __init__(self):
        self.balance = 5000
        self.daily_withdrawal_limit = 3000
        self.withdrawn_today = 0

    def show_menu(self):
        print("---" * 15)
        print("Welcome! Select an option:")
        print("(1) Withdraw   (2) Deposit")
        print("(3) Balance    (0) Exit")
        return int(input("Choose a number: "))

    def withdraw(self, amount):
        if amount > 3000:
            print("You'r account is restricted you can't withdraw more than 3000")
        elif amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Your balance now is {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print(f"Your balance now is {self.balance}")

    def check_balance(self):
        print(f"Your account balance is {self.balance}")

    def run(self):
        while True:
            selection = self.show_menu()
            if selection == 1:
                amount = int(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif selection == 2:
                amount = int(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif selection == 3:
                self.check_balance()
            elif selection == 0:
                print("Thank you! Have a great day.")
                break
            else:
                print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    account_type = int(input("Select an account type (1 = Normal/2 = Restricted): "))
    if account_type == 1:
        account = NormalAccount()
    elif account_type == 2:
        account = RestrictedAccount()
    else:
        print("Invalid account type. Defaulting to Normal Account.")
        account = NormalAccount()

    account.run()
