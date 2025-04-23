
from BankAccount import BankAccount

def bank_menu():
    print("Welcome to the Bank of Python!")
    name = input("Enter your name: ")
    current_account = BankAccount(name)

    current_account = BankAccount(name)

    for account in BankAccount.all_accounts:
        if account.account_holder == name:
            print(f"Welcome back, {name}!")
            break
        

    if __name__ == "__main__":
        ix = BankAccount("Ix", 1000)
        rose = BankAccount("Rose", 200000)
        tom = BankAccount("Tom", 9000)
