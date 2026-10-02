# EXERCISE: Analyze the ages of a store's customers
#
# A store wants to better understand its customers to help decide
# which audience to focus its marketing efforts on.
# Use the pandas library to calculate the customers' average age.
#
# Instructions:
# 1. Create a dictionary containing the customers' names and ages.
# 2. Create a pandas Series with ages as values and names as the index.
# 3. Display the Series.
# 4. Calculate and display the average age.
#
# Note: The average age is a starting point. Other customer data
# should also be considered when choosing a target audience.

import pandas as pd

# Create a dictionary containing customer names and ages.
data = {
    "Name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "Age": [25, 30, 22, 35, 28]
}

# Create a Series using customer names as the index.
age_series = pd.Series(data["Age"], index=data["Name"])

# Display the customers' ages.
print("Customer Ages:")
print(age_series)

# Calculate the average age.
average_age = age_series.mean()

# Display the result.
print("\nAverage Age:", average_age)
