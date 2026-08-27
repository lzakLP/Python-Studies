# Beecrowd 1010 - Simple Calculate
#
# Read the data of two products, containing:
# - Product code
# - Quantity of products
# - Unit price of the product
#
# Then, calculate and display the total amount to be paid.
#
# Input:
# The input contains two lines. Each line contains three values:
# product code, quantity, and unit price.
#
# Output:
# Print the amount to be paid, according to the following format:
# VALOR A PAGAR: R$ X.XX

parts = input().split()
code = int(parts[0])
quantity = int(parts[1])
price = float(parts[2])
cost1 = quantity * price


parts = input().split()
code = int(parts[0])
quantity = int(parts[1])
price = float(parts[2])
cost2 = quantity * price

TOTAL = cost1 + cost2

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")
