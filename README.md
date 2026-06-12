# Bank Account Project

A small Python banking example demonstrating object-oriented account management, transaction handling, inheritance, and custom exception handling.

## Project Structure

- `bank_accounts.py` - Core account classes and banking operations.
- `oop_project.py` - Interactive script for creating accounts and managing transactions.

## Features

- `BankAccount` class with:
  - `getBalance()` to display account balance
  - `deposit(amount)` to add funds
  - `withdraw(amount)` with balance validation
  - `transfer(amount, account)` to move funds between accounts
- Custom `BalanceException` for insufficient funds handling
- `InterestRewardsAccount` subclass that adds 5% interest on deposits
- `SavingsAccount` subclass that inherits interest rewards and charges a $5 withdrawal fee
- Interactive menu for account creation, deposit, withdrawal, and transfers

## Usage

Run the interactive manager:

```bash
python oop_project.py
```

Follow the prompts to:
- create a current account, interest rewards account, or savings account
- deposit funds
- withdraw funds
- transfer between accounts
- display all accounts and balances

## Notes

- Withdrawals and transfers validate available balance before proceeding.
- `SavingsAccount` withdraws an extra $5 fee per transaction.
- `InterestRewardsAccount` increases deposits by 5% automatically.
- The program continues until the user chooses to exit.

## License

This project is provided as-is for learning and demonstration purposes.
