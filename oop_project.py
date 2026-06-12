from bank_accounts import BankAccount, InterestRewardsAccount, SavingsAccount


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid value. Please enter a number.")


def select_account(accounts, prompt="Select account: "):
    if not accounts:
        print("No accounts available.")
        return None

    names = list(accounts.keys())
    for index, name in enumerate(names, start=1):
        account = accounts[name]
        print(f"{index}. {name} ({type(account).__name__}, Balance=${account.balance:.2f})")

    while True:
        selection = input(prompt).strip()
        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(names):
                return accounts[names[index]]
        elif selection in accounts:
            return accounts[selection]

        print("Invalid selection. Enter the account number or name.")


def create_account(accounts):
    name = input("Enter account holder name: ").strip()
    if not name:
        print("Account name cannot be empty.")
        return

    if name in accounts:
        print("An account with that name already exists.")
        return

    initial_amount = get_positive_float("Enter initial deposit amount: ")

    print("\nAccount types:")
    print("1. Current account")
    print("2. Interest rewards account")
    print("3. Savings account")

    while True:
        account_type = input("Choose account type [1-3]: ").strip()
        if account_type == "1":
            account = BankAccount(initial_amount, name)
            break
        elif account_type == "2":
            account = InterestRewardsAccount(initial_amount, name)
            break
        elif account_type == "3":
            account = SavingsAccount(initial_amount, name)
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    accounts[name] = account
    print(f"Account created for {name} ({type(account).__name__}).")


def show_accounts(accounts):
    if not accounts:
        print("No accounts have been created yet.")
        return

    print("\nCurrent accounts:")
    for account in accounts.values():
        account.getBalance()


def deposit_to_account(accounts):
    account = select_account(accounts, "Enter account to deposit into: ")
    if account:
        amount = get_positive_float("Deposit amount: ")
        account.deposit(amount)


def withdraw_from_account(accounts):
    account = select_account(accounts, "Enter account to withdraw from: ")
    if account:
        amount = get_positive_float("Withdrawal amount: ")
        account.withdraw(amount)


def transfer_between_accounts(accounts):
    if len(accounts) < 2:
        print("At least two accounts are required to transfer funds.")
        return

    print("\nSource account:")
    source = select_account(accounts, "Select the source account: ")
    if not source:
        return

    print("\nDestination account:")
    destination = select_account(accounts, "Select the destination account: ")
    if not destination:
        return

    if source is destination:
        print("Source and destination cannot be the same account.")
        return

    amount = get_positive_float("Transfer amount: ")
    source.transfer(amount, destination)


def print_menu():
    print("\n=== Bank Account Manager ===")
    print("1. Create an account")
    print("2. Show all accounts")
    print("3. Deposit funds")
    print("4. Withdraw funds")
    print("5. Transfer funds")
    print("6. Exit")
    return input("Choose an option [1-6]: ").strip()


def main():
    accounts = {}

    while True:
        choice = print_menu()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            show_accounts(accounts)
        elif choice == "3":
            deposit_to_account(accounts)
        elif choice == "4":
            withdraw_from_account(accounts)
        elif choice == "5":
            transfer_between_accounts(accounts)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

