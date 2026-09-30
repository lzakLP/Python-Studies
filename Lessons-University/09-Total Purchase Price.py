# EXERCISE: CALCULATING THE TOTAL PURCHASE PRICE
#
# Develop a Python program for a friend's store.
# Ask how many different items the customer is purchasing.
# For each item, read its unit price and purchased quantity.
# Store unit prices and quantities in separate lists.
#
# Create a function named calculate_total_price that:
# 1. Receives the prices, quantities, and a mutable result container.
# 2. Multiplies each unit price by its corresponding quantity.
# 3. Adds these amounts and updates the result container directly,
#    without returning the calculated total.
#
# Call the function and display the total in Brazilian reais (R$),
# formatted to two decimal places.
# Assume positive item counts and quantities, and nonnegative prices.
#
# PYTHON NOTE:
# Arguments are passed by object sharing. A one-element list lets the
# function change a result that the caller can access. This demonstrates
# shared mutation without using C-style pointers.

from math import isfinite


def calculate_total_price(unit_prices, quantities, total_price):
    # Reset the value inside the shared list before calculating.
    total_price[0] = 0.0

    # The input lists have matching positions for each purchased item.
    for price, quantity in zip(unit_prices, quantities):
        total_price[0] += price * quantity


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid input. Enter a whole number greater than zero.")


def read_unit_price(prompt):
    while True:
        try:
            price = float(input(prompt))
            if isfinite(price) and price >= 0:
                return price
        except ValueError:
            pass
        print("Invalid price. Enter a nonnegative number (example: 12.50).")


def main():
    num_items = read_positive_integer("Enter the number of different items: ")

    unit_prices = []
    quantities = []

    # Collect the unit price and quantity of each item.
    for index in range(num_items):
        print(f"\nItem {index + 1}")
        unit_prices.append(read_unit_price("Enter the unit price (R$): "))
        quantities.append(read_positive_integer("Enter the quantity: "))

    # Use a mutable container to hold the result calculated by the function.
    total_price = [0.0]
    calculate_total_price(unit_prices, quantities, total_price)

    # Read the updated value from the same list.
    print(f"\nTotal purchase price: R$ {total_price[0]:.2f}")


if __name__ == "__main__":
    main()
