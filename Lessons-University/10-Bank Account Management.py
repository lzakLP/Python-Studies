# CASE STUDY: BANK ACCOUNT MANAGEMENT
#
# Develop a Python program that simulates basic banking operations.
# Each account must have a number, an account holder, and a balance.
# Start with two accounts: account 1 with R$ 1000.00 and account 2
# with R$ 500.00.
#
# Display both balances and a menu with the following options:
# 1. Deposit money into an account.
# 2. Withdraw money if sufficient funds are available.
# 3. Transfer money between the two accounts.
# 4. Exit the program.
#
# Use functions that update the account objects directly.
# Reject invalid accounts, nonpositive amounts, fractions of a cent,
# insufficient funds, and transfers to the same account.
# Failed operations must leave the balances unchanged.
# Display clear messages and format monetary values to two decimal places.
#
# PYTHON NOTE:
# Arguments are passed by object sharing. Updating an Account object's
# balance changes the same object accessed by the caller.

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

CENT = Decimal("0.01")
AMOUNT_ERROR = "Enter a positive amount in whole cents (example: 25.50)."


@dataclass
class Account:
    number: int
    holder: str
    balance: Decimal


def is_valid_amount(amount):
    try:
        return (
            amount.is_finite()
            and amount > 0
            and amount == amount.quantize(CENT)
        )
    except InvalidOperation:
        return False


def deposit(account, amount):
    if not is_valid_amount(amount):
        print(AMOUNT_ERROR)
        return False

    account.balance += amount
    return True


def withdraw(account, amount):
    if not is_valid_amount(amount):
        print(AMOUNT_ERROR)
        return False

    if account.balance < amount:
        print("Insufficient funds. The operation was not completed.")
        return False

    account.balance -= amount
    return True


def transfer(source, destination, amount):
    if source.number == destination.number:
        print("Source and destination accounts must be different.")
        return False

    # Credit the destination only after a successful withdrawal.
    if withdraw(source, amount):
        deposit(destination, amount)
        return True

    return False


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a whole number.")


def read_amount():
    while True:
        try:
            # Create Decimal directly from text to preserve decimal precision.
            amount = Decimal(input("Amount (R$): "))

            if is_valid_amount(amount):
                return amount.quantize(CENT)

        except InvalidOperation:
            pass

        print(AMOUNT_ERROR)


def choose_account(accounts, prompt):
    account = accounts.get(read_integer(prompt))

    if account is None:
        print("Account not found. Choose account 1 or 2.")

    return account


def main():
    accounts = {
        1: Account(1, "Customer 1", Decimal("1000.00")),
        2: Account(2, "Customer 2", Decimal("500.00")),
    }

    while True:
        print("\nBOLSOFURADO BANK\n")

        for account in accounts.values():
            print(
                f"Account {account.number} - {account.holder}: "
                f"R$ {account.balance:.2f}"
            )

        print("\n1 - Deposit")
        print("2 - Withdraw")
        print("3 - Transfer")
        print("4 - Exit")

        option = read_integer("Choose an option: ")

        if option == 1:
            account = choose_account(
                accounts, "Deposit into account: "
            )

            if account is not None and deposit(account, read_amount()):
                print("Deposit completed successfully.")

        elif option == 2:
            account = choose_account(
                accounts, "Withdraw from account: "
            )

            if account is not None and withdraw(account, read_amount()):
                print("Withdrawal completed successfully.")

        elif option == 3:
            source = choose_account(accounts, "Source account: ")
            if source is None:
                continue

            destination = choose_account(
                accounts, "Destination account: "
            )
            if destination is None:
                continue

            if source.number == destination.number:
                print("Source and destination accounts must be different.")
                continue

            if transfer(source, destination, read_amount()):
                print("Transfer completed successfully.")

        elif option == 4:
            print("Program ended.")
            break

        else:
            print("Invalid option. Choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
