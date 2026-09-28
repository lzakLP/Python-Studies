# ACTIVITY: DISCOUNT CALCULATOR
#
# Develop a Python program that helps salespeople calculate
# the final purchase price after applying a discount.
#
# The program must follow these steps:
#
# 1. Ask the user to enter the product price in US dolars.
#    Prompt: "Enter the product price: $ "
#
# 2. Ask the user to enter the discount percentage.
#    Prompt: "Enter the discount percentage: "
#
# 3. Convert the inputs to float to support decimal numbers.
#
# 4. Check whether the percentage is between 0 and 100, inclusive.
#    If it is outside this range, display an error message
#    and do not perform the calculation.
#
# 5. If the percentage is valid, calculate the discount amount:
#    discount = product price * (discount percentage / 100)
#
# 6. Calculate the final purchase price:
#    final price = product price - discount
#
# 7. Display the final price with two decimal places, preceded
#    by the message "Discounted price: $ ".
#
# EXAMPLE RUN:
# Enter the product price: $ 150
# Enter the discount percentage: 12.5
# Discounted price: $ 131.25
#
# TIPS:
# - Use input() to receive user input.
# - Use if and else to validate the percentage.
# - Use an f-string with :.2f to format the result.
# - Use a period as the decimal separator when entering numbers.
#
# Write your code below:

# Ask for the product price and discount percentage.
product_price = float(input("Enter the product price: $ "))
discount_percentage = float(input("Enter the discount percentage: "))

# Check whether the discount percentage is within the valid range.
if discount_percentage < 0 or discount_percentage > 100:
    print("Error: The discount percentage must be between 0 and 100.")
else:
    # Calculate the discount amount.
    discount = product_price * (discount_percentage / 100)

    # Calculate the final purchase price.
    final_price = product_price - discount

    # Display the final price with two decimal places.
    print(f"Discounted price: $ {final_price:.2f}")
